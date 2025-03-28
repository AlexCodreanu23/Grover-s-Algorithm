# Grover's Algorithm

Descriere:
Algoritmul lui Grover eficientizează problema de căutare pentru un set de date neordonate folosind mai puţini paşi decât oricare alt algoritm clasic.  Acest algoritm a fost conceput de Lov Grover in 1996. Algoritmul găseşte un singur element marcat într-un set de n elemente în complexitatea O(log(N)). Un algoritm clasic de căutare ar avea complexiatea O(N/2).

Aplicații
Algoritmul lui Grover este aplicabil petru orice problemă care poate fi redusă la verificarea validității unei valori date, de exemplu căutarea într-un set de date, factorizarea numerelor întregi, rezolvarea formulelor booleene și Traveling Salesman Problem.
Algoritmul Grover poate fi utilizat pentru a decoda chei criptografice considerate sigure, pentru diverse atacuri brute-force asupra criptografiei cu cheie simetrică, inclusiv atacuri de coliziune și atacuri pre-imagine. De exemplu, ar putea decoda o cheie criptografică simetrică de 128 de biţi folosind brute-force în aproximativ 264 iteraţii şi o cheie de 256 de biţi în ≈2128 iteraţii. Acest lucru prezintă un risc pentru securitatea tranzacțiilor online și comunicațiilor.
Mai poate fi utilizat pentru a rezolva probleme de optimizare care sunt dificile sau imposibil de rezolvat cu un computer clasic.  Poate găsi mult mai eficient cel mai scurt drum între două puncte sau poate determina ce investiţii vor fi cele mai profitabile. De asemenea, poate fi folosit pentru detectarea activităţilor online illegale sau pentru diagnosticarea unor afecțiuni cum ar fi identificarea celulelor canceroase. 
În domeniul învățării automate (machine learning) acest algoritm poate fi folosit pentru a eficientiza găsirea unor soluţii sau datelor relevante în baze mari de date.

Limitări
Acest algoritm nu este încă practic deoarece necesită un număr mare de qubiţi pentru unele aplicaţii, iar in actualitate, calculatoarele cuantice nu sunt destul de avansate. Algoritmul lui Grover oferă un avantaj semnificativ doar pentru problemele care au un spațiu mare de căutare. Pentru probleme cu seturi de date mai restrânse, eficientizarea nu este destul de semnificativă pentru a justifica utilizarea acestuia. 
La fel ca orice algoritm cuantic, algoritmul lui Grover este susceptibil la erori generate de noise– cauzat de interferenţe ale altor dispozitive, câmpuri magnetice şi interacţiuni între qubiţi; şi decoherence– colapsul superpoziţiei.

Etapele Algoritmului Grover:
1. Starea inițială – Toate numerele sunt în suprapunere
●	Algoritmul începe cu un registru cuantic reprezentând un șir de N elemente (în acest exemplu, avem 8 numere).
●	Fiecare stare cuantică corespunde unui număr din șir.
●	Aplicăm poarta Hadamard pe fiecare qubit, ceea ce creează o suprapunere uniformă a tuturor stărilor posibile.
●	În această stare inițială, fiecare număr are aceeași amplitudine și, implicit, aceeași probabilitate de apariție la măsurare.

![2](https://github.com/user-attachments/assets/d42accf2-3eb0-48a5-9cd4-3b63d8d7842b)


2. Inversarea fazei pentru numărul căutat
●	Oracle-ul este o funcție cuantică care marchează numărul pe care dorim să îl găsim.
●	Acest lucru se face prin inversarea fazei stării cuantice corespunzătoare numărului căutat.
●	În termeni vizuali, dacă amplitudinea inițială a tuturor stărilor era pozitivă, după aplicarea oracle-ului, amplitudinea numărului căutat devine negativă, în timp ce celelalte rămân neschimbate.

![3](https://github.com/user-attachments/assets/69a8d05b-25c5-433c-950d-1f48cd89aff3)


3. Operatorul Grover crește probabilitatea numărului căutat
●	Se aplică operatorul de difuzie Grover, care este un fel de „reflecție față de medie”.
●	Acesta funcționează astfel: 
  1.	Calculează media amplitudinilor tuturor stărilor.
  2.	Ajustează amplitudinile astfel încât valorile deja mici scad și mai mult, iar valoarea numărului căutat crește.
●	Aceasta este cheia algoritmului: în loc să căutăm numărul în mod clasic, creștem probabilitatea de a-l găsi prin amplificarea amplitudinilor sale.

![4](https://github.com/user-attachments/assets/dfc9ddab-0f69-4d97-9b77-f4e66b5bd673)

4. Creșterea progresivă a amplitudinii numărului căutat
  ●	Pasul 2 (Oracle-ul) și pasul 3 (Amplificarea amplitudinilor) sunt repetate de un număr optim de ori, calculat ca O(radical din N)
  ●	De fiecare dată, amplitudinea numărului căutat crește progresiv, ceea ce înseamnă că probabilitatea de a-l măsura corect crește exponențial.

![5](https://github.com/user-attachments/assets/4cbabc4b-d1b3-4780-a0ac-e2e2fee326ba)

5. Probabilitățile finale după aplicarea Grover
●	După suficiente iterații, amplitudinea numărului căutat este mult mai mare decât celelalte.
●	Când măsurăm registrul cuantic, numărul căutat are cea mai mare probabilitate să fie observat.
●	Practic, algoritmul Grover face ca numărul corect să fie selectat cu aproape 100% probabilitate.

![6](https://github.com/user-attachments/assets/0e4754b7-b43b-40f3-a784-5c87a6d859b8)


6. Implementarea pe IBM Q – Histogramă a măsurătorilor
●	Algoritmul este implementat pe un calculator cuantic real (IBM Quantum Computer).
●	După rularea circuitului de mai multe ori (de exemplu, 1024 măsurători), se generează o histogramă a măsurătorilor.
●	Într-un calculator cuantic real, există erori hardware, astfel că rezultatele pot să nu fie perfect precise, dar vor fi destul de apropiate de teorie.

![7](https://github.com/user-attachments/assets/0486b40e-7a79-4df5-8e1b-8989d7b1847e)

Implementarea Algoritmului Lui Grover pe IBM Quantum :

![8](https://github.com/user-attachments/assets/22604d2e-8d00-4a91-af79-6482744045a8)
![9](https://github.com/user-attachments/assets/f8408fb2-6d4e-486a-b6f5-656bf5961b79)
![10](https://github.com/user-attachments/assets/77fa757a-bb42-4fc7-941d-3250f6ea76a4)


