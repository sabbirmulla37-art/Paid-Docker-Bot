import subprocess
import os

class DockerManager:
    def __init__(self):
        # Counter file track karega ki agla VPS kis number se banega
        self.counter_file = "vps_counter.txt"
        
    def _get_next_vps_number(self):
        """Har naye VPS ke liye unique number generate karega (1, 2, 3...)"""
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f:
                f.write("1")
            return 1
        
        with open(self.counter_file, "r") as f:
            try:
                current = int(f.read().strip())
            except ValueError:
                current = 1
                
        next_num = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(next_num))
        return next_num

    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

    def create_vps_for_user(self):
        """Har naye user ke liye unique number wala container banayega"""
        vps_id = self._get_next_vps_number()
        container_name = f"vps_user_{vps_id}"
        
        # Ubuntu container start karega jo background mein chalega
        cmd = f"docker run -d --name {container_name} ubuntu:20.04 sleep infinity"
        output = self.run_command(cmd)
        
        if "Error" in output:
            return f"Failed to create VPS: {output}"
        
        return f"Success! VPS Created. Container Name/Number: {container_name}"

    def stop_vps(self, container_name):
        return self.run_command(f"docker stop {container_name}")

    def remove_vps(self, container_name):
        return self.run_command(f"docker rm -f {container_name}")

# Example usage:
if __name__ == "__main__":
    manager = DockerManager()
    # Jab bhi aap naya VPS banaoge, yeh automatic agla number de dega (vps_user_1, vps_user_2...)
    print(manager.create_vps_for_user())
    
