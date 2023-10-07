import re
import string

class PreProcLight:
    def __init__(self):
        self.spec_chars = ["\n", "\t", "\r", "<br>"]

    def remove_links(self, text):
        # remove https links
        return re.sub(r"https\S+","", text)

    def remove_calls(self, text):
        # remove @text
        return re.sub(r"@\S+","", text)

    def remove_punctuation(self, text):
        # remove special chars
        return re.sub(f"[{re.escape(string.punctuation)}]", '', text)

    def remove_chars(self, text):
        # remove special chars
        for char in self.spec_chars:
            text = text.replace(char, "")
        return text

    def remove_digits(self, text):
        # remove digits
        return re.sub(r"\d", "", text)

    def remove_emojis(self, text):
        # remove emojis
        emoj = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002500-\U00002BEF"  # chinese char
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            u"\U0001f926-\U0001f937"
            u"\U00010000-\U0010ffff"
            u"\u2640-\u2642" 
            u"\u2600-\u2B55"
            u"\u200d"
            u"\u23cf"
            u"\u23e9"
            u"\u231a"
            u"\ufe0f"  # dingbats
            u"\u3030"
                        "]+", re.UNICODE)
        return re.sub(emoj, '', text)

    def clean_text(self, text):
        if text == None:
            return ""
        text = self.remove_links(text)
        text = self.remove_calls(text)
        text = self.remove_chars(text)
        text = self.remove_digits(text)
        text = self.remove_emojis(text)
        text = self.remove_punctuation(text)
        text = text.lower()

        return text