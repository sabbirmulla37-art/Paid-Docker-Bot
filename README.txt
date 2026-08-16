PrimeCloud VPS Bot - Setup

1. Install requirements:
   pip install -r requirements.txt

2. Install Docker on the VPS host and make sure the bot user can run `docker`.

3. Open bot.py and replace ONLY:
   primecloud_token_here
   with your Discord bot token.

4. Optional public IP/hostname:
   export PUBLIC_IP="YOUR_SERVER_PUBLIC_IP"
   If PUBLIC_IP is not set, bot.py currently uses its configured fallback.

5. Run:
   python3 bot.py

Files:
- bot.py
- admin_data.json
- requirements.txt

admin_data.json already contains the current main admin ID configured in bot.py.
Do not share your bot token.
