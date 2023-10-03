def remove_links(v):
    # remove https links
    return re.sub(r"https\S+","", v)

def remove_calls(v):
    # remove @text
    return re.sub(r"@\S+","", v)

def remove_punctuation(v):
    # remove special chars
    return re.sub(f"[{re.escape(string.punctuation)}]", '', v)

def remove_chars(v):
    # remove special chars
    chars = ["\n", "\t", "\r", "<br>"]
    for char in chars:
        v = v.replace(char, "")
    return v

def remove_digits(v):
    # remove digits
    return re.sub(r"\d", "", v)

def remove_emojis(data):
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
    return re.sub(emoj, '', data)

    
df.Text = df.Text.apply(remove_links)
df.Text = df.Text.apply(remove_calls)
df.Text = df.Text.apply(remove_punctuation)
df.Text = df.Text.apply(remove_chars)
df.Text = df.Text.apply(remove_digits)
df.Text = df.Text.apply(remove_emojis)

# lower the text
df.Text = df.Text.str.lower()
# remove rows with the text too short
min_text_len = 20
df = df[~df.Text.str.len()<min_text_len].reset_index(drop=True)
print("preprocess completed")