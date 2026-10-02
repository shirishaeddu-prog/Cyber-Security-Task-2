# Task 2: Phishing Email Analysis

import re

# Sample suspicious email
email = """
From: security-alert@paypa1-support.com
To: user@gmail.com
Subject: URGENT! Your account will be blocked

Dear Customer,

Your account has been suspended.
You must verify your account immediately within 24 hours.

Click here to verify:
http://paypa1-login.example.com/verify

If you do not verify your account, your account will be permanently blocked.

Thank you,
Account Security Team
"""

print("PHISHING EMAIL ANALYSIS")
print("-----------------------")

print("\nEmail Sample:")
print(email)

# Check sender
if "paypa1" in email.lower():
    print("1. Suspicious sender address found.")

# Check urgent words
urgent_words = ["urgent", "immediately", "24 hours", "blocked", "suspended"]

for word in urgent_words:
    if word.lower() in email.lower():
        print("2. Urgent/threatening language found:", word)
        break

# Check links
links = re.findall(r'https?://\S+', email)

if links:
    print("3. Suspicious link found:")
    for link in links:
        print("   ", link)

# Check spelling/domain
if "paypa1" in email.lower():
    print("4. Possible spoofed domain detected.")

# Check request for verification
if "verify" in email.lower():
    print("5. Account verification request found.")

# Final result
print("\n-----------------------")
print("ANALYSIS RESULT")
print("-----------------------")
print("Phishing indicators found:")
print("- Suspicious sender/domain")
print("- Urgent and threatening language")
print("- Suspicious verification link")
print("- Request for immediate account action")

print("\nConclusion:")
print("The email shows multiple phishing characteristics.")
print("Users should not click the link or provide personal information.")