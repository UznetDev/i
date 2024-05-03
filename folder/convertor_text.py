def convertor(text: str, f_words: list[str]):
  for i in f_words:
    if i.lower() in text.lower():
      text = text.lower().replace(i.lower(), '*'*len(i))
  return text

def censor_words(text_file, forbidden_words_file):
  with open(forbidden_words_file, 'r') as f:
    forbidden_words = f.read().split()
  with open(text_file, 'r') as f:
    text = f.read().split()
  foldeer = []
  for i in text:
    tx = convertor(i, forbidden_words)
    text = ''
    for x in range(len(i)):
        text += tx[x] if tx[x] == '*' else i[x]
    foldeer.append(text)
  return ' '.join(foldeer)


text_file = 'text.txt'
forbidden_words_file = 'forbidden_words.txt'
censored_text = censor_words(text_file, forbidden_words_file)
print(censored_text)