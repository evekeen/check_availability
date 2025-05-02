# Usage
```
python helmet_checker.py https://www.motoland.rs/proizvod/31153/shoei-nxr-ii-white
```

# Email Notifications
```
python helmet_checker.py https://www.motoland.rs/proizvod/31153/shoei-nxr-ii-white --email your_email@example.com
```

For sending emails, set these environment variables:
```
export EMAIL_ADDRESS="your_gmail@gmail.com"
export EMAIL_PASSWORD="your_app_password"
```

Note: For Gmail, you'll need to use an App Password instead of your regular password. [Generate one here](https://myaccount.google.com/apppasswords).

# Scheduling Options

## Option 1: Using cron (macOS/Linux)
1. Make the script executable: `chmod +x run_daily.sh`
2. Edit the email addresses and credentials in `run_daily.sh`
3. Set up cron job: `crontab -e` and add:
   ```
   0 8 * * * /absolute/path/to/run_daily.sh >> /absolute/path/to/helmet_checker.log 2>&1
   ```

## Option 2: Using GitHub Actions
1. Push your code to a GitHub repository
2. Set up repository secrets:
   - `RECIPIENT_EMAIL`: Your email address to receive notifications
   - `EMAIL_ADDRESS`: Your sender Gmail address
   - `EMAIL_PASSWORD`: App password for your Gmail account
3. The workflow will run daily at 8:00 AM UTC

## Option 3: SMS Notifications (Twilio)
1. Install Twilio: `pip install twilio`
2. Update your run_daily.sh to call the SMS script or modify helmet_checker.py
3. Example usage:
   ```
   python sms_notification_setup.py "Helmet available!" "+1234567890" --account_sid "your_sid" --auth_token "your_token" --twilio_number "+1987654321"
   ```