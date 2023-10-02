# :construction: README em construção ! :construction:

# Project Algorithms

#### This project consists of six challenges proposed by Trybe for solving and optimizing algorithms, applying the concepts of recursion and iterativity; time and space complexity; applying search and sorting algorithms that are not native to Python and carrying out tests.

* Solved using Python

<details>
<summary>Description of created solutions:</summary>
<br>
  
| Function | Description | Location |
| ----------- | ----------- | ----------- |
| `study_schedule`   | Returns number of students online at the times informed in array of tuples as `permanence_period` compared to the time informed as `target_time` | `challenges/challenge_study_schedule.py` |
| `is_palindrome_recursive`   |  Evaluate whether a word is palindromic, in a recursive way| `challenges/challenge_palindromes_recursive.py` |
| `is_anagram`   | Evaluate whether the words informed are anagrams | `challenges/challenge_anagrams.py` |
| `find_duplicate`   | - | `challenges/challenge_find_the_duplicate.py` |
| `is_palindrome_iterative`   | - | `challenges/challenge_palindromes_interative.py` |

</details>

<details>
<summary>Description of created test:</summary>
<br>
  
| Test | Description | Location |
| ----------- | ----------- | ----------- |
| `test_encrypt_message`   | test... | `tests/encrypt/test_encrypt.py` |

</details>


## Structure of project
  ```
  .
  ├── challenges
  │   ├──🔹 challenge_anagrams.py
  │   ├──🔸 challenge_encrypt_message.py
  │   ├──🔹 challenge_find_the_duplicate.py
  │   ├──🔹 challenge_palindromes_iterative.py
  │   ├──🔹 challenge_palindromes_recursive.py
  │   └──🔹 challenge_study_schedule.py
  ├── tests
  │   ├── encrypt
  │   │   ├──🔸 __init__.py
  │   │   ├──🔸 conftest.py
  │   │   ├──🔸 mocks.py
  │   │   └──🔹 test_encrypt.py
  │   ├── results
  │   │   └──🔸 .gitignore
  │   ├──🔸 __init__.py
  │   ├──🔸 complexities.py
  │   ├──🔸 generators.py
  │   ├──🔸 marker.py
  │   ├──🔸 test_anagrams.py
  │   ├──🔸 test_find_the_duplicate.py
  │   ├──🔸 test_palindromes_iterative.py
  │   ├──🔸 test_palindromes_recursive.py
  │   └──🔸 test_study_schedule.py
  ├──🔸 dev-requirements.txt
  ├──🔸 pyproject.toml
  ├──🔸 README.md
  ├──🔸 requirements.txt
  ├──🔸 setup.cfg
  ├──🔸 setup.py
  ├──🔸 trybe-filter-repo.sh
  └──🔸 trybe.yml

Legenda:
  🔸 Arquivos que não podem ser alterados.
  🔹 Arquivos a serem alterados para realizar os requisitos.
```

<!---
### Instructions
* To run the repository locally, clone the project and use the following commands to initialize Docker:
  
  ```
  docker-compose up -d // start application with docker
  docker attach one_for_all
  npm install // install dependencies
  docker-compose down // stop application
  ```
-->


