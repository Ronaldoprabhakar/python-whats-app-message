import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
admin_mail = input("Enter admin E-mail ID:")
admin_password = input("Enter admin E-mail password:")
server.login(admin_mail, admin_password)
send_from = input("Enter sender E-Mail ID:")
send_to = input("Enter receiver E-Mail ID:")
message = input("Enter text message:")
server.sendmail(send_from,send_to, message)
print("sucessfully runned")
server.quit()

