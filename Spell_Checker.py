from spellchecker import SpellChecker as PySpellChecker
import logging


# File handler and stream handler setup
logger = logging.getLogger("Spell_Checker_Logger")
logger.setLevel(logging.DEBUG)

if logger.hasHandlers():
    logger.handlers.clear()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)  
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler("spell_checker.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


class TextSpellChecker:
    def __init__(self):
        self.spell = PySpellChecker()


    def correct_text(self,text):
        words = text.split()
        corrected_words = []

        for word in words:
            try:

                corrected = self.spell.correction(word)                            
                if corrected is None:
                    logger.warning(f"No suggestion found for '{word}'")
                    corrected_words.append(word)

                else:
                    if corrected != word.lower():
                        logger.info(f"Correction '{word}' to '{corrected}'")
                    corrected_words.append(corrected)

            except Exception as e:
                logger.error(f"Error correcting word '{word}' : {e}")
                corrected_words.append(word)

        return ' '.join(corrected_words)
        
    
    def run(self):
        print("\n----- Text Spell Checker -----")
        while True:
            try:

                text = input("Enter text to check (or type 'exit' to quit): ")
                if text.lower() == "exit":
                    logger.info("Program exited by user...")
                    break


                corrected_text = self.correct_text(text)
                print(f"Corrected Text is : {corrected_text}")
                logger.info(f"Corrected Text is : {corrected_text}")
            
            except Exception as e:
                logger.critical(f"Unexpected error : {e}")


if __name__ == "__main__":
    TextSpellChecker().run()
