# labb3

Uppgift 1: Kopiera textfil
Skapa funktionen copy_text_file(in_file, out_file) som läser in filen in_file, och skriver ut en kopia i en fil som heter out_file.

I denna uppgift kan ni anta att filen in_file existerar och är på rätt format.

Testa er funktion genom att köra: copy_text_file("namn.csv", "my_copy.csv")

Uppgift 2: Kryptera textfil
Skapa funktionen encrypt_file(in_file, out_file) läser in filen in_file, krypterar den med hjälp av modulen text_encryption_function.py, samt skriver ut resultatet i en fil som heter out_file.

Notera att funktionen för kryptering, encrypt, redan finns, men skall anropas av er från my_module.py.

I denna uppgift kan ni anta att filen in_file existerar och är på rätt format.

Testa er funktion genom att köra encrypt_file("namn.csv", "secret_names.csv")

Notera att lösningen på denna uppgift är mycket lik lösningen på Uppgift 1 ovan.

Uppgift 3: Kryptering med felhantering
Skapa en funktion user_dialogue() som ber om namn på två filer, och kör er egen funktion encrypt_file (från Uppgift 2) på dessa två filer. Er nya funktion (user_dialogue) skall ha felhantering, och fånga upp om in_file inte existerar, och i sådana fall fråga efter ett nytt filnamn. Se följande exempel:

Name of new encrypted file:out_file.txt
Name of file to be encrypted:blaha.txt
That resulted in an input/output error, please try again! Details:FileNotFoundError(2, 'No such file or directory')
Name of file to be encrypted:namn.csv
Encryption completed!
Notera att felhanteringen skall ske i user_dialogue, trots att själva felet (om filen inte existerar) uppkommer i encrypt_file. Ni skall inte ändra i encrypt_file.

Notera även att utskriften kan variera något vad gäller det som kommer efter "Details:", t.ex. [Errno 2] No such file or directory: 'blaha.txt', eller liknande är helt ok.

Uppgift 4: Heltal med felhantering
Skapa en funktion get_int_input(prompt_string) som gör ungefär samma sak som 

int(input(prompt_string)), men med felhantering. Följande exempel visar hur det kan se ut om man kör get_int_input("Ange ett tal:")

Ange ett tal:hej
Svara med ett heltal!
Ange ett tal:åtta
Svara med ett heltal!
Ange ett tal:4
Notera att lösningarna till uppgift 3 och 4 ovan ofta är allt som behövs för att gå från betyg D till C på P-uppgiften.

Uppgift 5: Ett Quiz-spel
Skapa en quiz-spel som beter sig enligt följande:


----------------------------------------
Hello and welcome to the quiz!
----------------------------------------
Vad heter Norges huvudstad?
Alternativ 1: Bergen , Alternativ 2: Oslo , Alternativ 3: Köpenhamn
Vilket är ditt svar? (1,2,3):blaha
Svara med ett heltal!
Vilket är ditt svar? (1,2,3):3
Fel, det rätta svaret är: Oslo
----------------------------------------
Vad står ABBA för?
Alternativ 1: Smarrig Sill , Alternativ 2: Kalle och Lisa , Alternativ 3: Agneta Björn Benny Annefrid
Vilket är ditt svar? (1,2,3):3
Rätt, det är: Agneta Björn Benny Annefrid

I denna uppgift kan ni använda följande lista av listor för själva frågorna

short_quiz_list_of_lists = [['Vad heter Norges huvudstad?', 'Oslo', 'Bergen', 'Köpenhamn'],
['Vad står ABBA för?', 'Agneta Björn Benny Annefrid', 'Kalle och Lisa', 'Smarrig Sill']]
Notera att varje element i listan är en lista på formatet [fråga, alt1, alt2, alt3], där alternativ 1 alltid är det rätta.

Ni skall alltså skriva en funktion run_quiz(quiz_list_of_lists) som

skriver ut en tjusig rubrik "Hello and welcome..."
skriver ut en fråga och alternativen
be om ett svar med hjälp av er funktion i Uppgift 4
berätta om det var rätt eller fel 
(osv så länge det finns nya frågor)
Notera att det blir lite tråkigt om alternativ 1 alltid är rätt, så för att göra det mer spännande kan ni blanda om alternativen (t.ex. med random.shuffle(list)), men det är inte ett krav.

Uppgift 6: Inläsning av data till Quiz-spel med felhantering
Skapa en funktion get_quiz_list_handle_exceptions() som läser in en fil av typen quiz.csv och skapar en lista av listor av typen short_quiz_list_of_lists.

Användbara funktioner är

string.strip() - tar bort skräptecken
string.split(";") - delar upp sträng separerad av ";" i lista
Felhanteringen skall fånga upp både icke-existerande filer, och filer som inte innehåller rader med fyra delar separerade av ;

Exempel på användardialog:

Name of quiz-file: hejsan
That resulted in an input/output error, please try again!
Name of quiz-file: namn.csv
The file is not on the proper format. There needs to be four strings, separated by ; in each line of the file.
Name of quiz-file: quiz.csv

Uppgift 7: Quiz-spel med data från fil och felhantering
Kombinera uppgift 5 och 6 till ett tjusigt Quiz-spel. Lägg till en fråga i filen quiz.csv och se till att den kommer med i spelet. 


Name of quiz-file: namn.csv
The file is not on the proper format. There needs to be four strings, separated by ; in each line of the file.
Name of quiz-file: quiz.csv
----------------------------------------
Hello and welcome to the quiz!
----------------------------------------
Vad heter Norges huvudstad?
Alternativ 1: Köpenhamn , Alternativ 2: Oslo , Alternativ 3: Bergen
Vilket är ditt svar? (1,2,3):haha
Svara med ett heltal!
Vilket är ditt svar? (1,2,3):2
Rätt, det är: Oslo
----------------------------------------
Vad står ABBA för?
Alternativ 1: Kalle och Lisa , Alternativ 2: Agneta Björn Benny Annefrid , Alternativ 3: Smarrig Sill
Vilket är ditt svar? (1,2,3):1
Fel, det rätta svaret är: Agneta Björn Benny Annefrid
----------------------------------------
När dog Karl XII?
Alternativ 1: 1718 , Alternativ 2: 1818 , Alternativ 3: 1717
Vilket är ditt svar? (1,2,3):
Uppgift 8: Json-filer
Lägg till import json längst upp i filen och kör koden nedan. Vad gör den? Vad är skillnaden på quiz.csv och den fil som skapas nedan? Vilken version gillar ni bäst?

ql = get_quiz_list_handle_exceptions()
json_string = json.dumps(ql, indent=2)
fo = open("quiz.json", "w")
fo.write(json_string)
fo.close()
