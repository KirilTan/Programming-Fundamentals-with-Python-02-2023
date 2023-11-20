class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


# Input
emails_list = []

command = input()
while command != "Stop":

    sender, receiver, content = command.split()
    emails_list.append(Email(sender, receiver, content))

    command = input()

# Send emails
sent_emails_indexes = [int(s) for s in input().split(", ")]

for current_sent_email_index in sent_emails_indexes:
    emails_list[current_sent_email_index].send()

# Output
for current_email in emails_list:
    print(current_email.get_info())
