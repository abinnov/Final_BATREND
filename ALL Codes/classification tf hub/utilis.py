from emoji import UNICODE_EMOJI
import unidecode

def remove_emoji(text):
  to_replace = UNICODE_EMOJI["en"]
  result = text
  for x in to_replace:
      result = result.replace(x, "")
  return result

def remove_accents(text):
  return unidecode.unidecode(text)
