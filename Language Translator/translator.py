from googletrans import Translator, LANGUAGES

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def main():
    print("Available Languages:")
    for code, lang in LANGUAGES.items():
        print(f"{code}: {lang}")

    while True:
        try:
            text = input("\nEnter the text you want to translate: ")

            src_lang = input("Enter the source language code (leave blank for auto-detect): ")
            if src_lang == '':
                src_lang = 'auto'
            elif src_lang not in LANGUAGES and src_lang != 'auto':
                print("Invalid source language code.")
                continue

            dest_lang = input("Enter the destination language code (e.g., 'es' for Spanish): ")
            if dest_lang not in LANGUAGES:
                print("Invalid destination language code.")
                continue

            translated_text = translate_text(text, src_lang, dest_lang)

            print(f"Translated text: {translated_text}")

            cont = input("Do you want to translate another text? (yes/no): ").lower()
            if cont != 'yes':
                print("Goodbye!")
                break

        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == '__main__':
    main()