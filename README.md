# Narzędzia usprawniające pracę z Pythonem

1. [better-exceptions](https://github.com/Qix-/better-exceptions)
  - Czyni wyjątki bardziej czytelnymi oraz wyświetla więcej informacji.
  - Pomaga znaleźć dziwne błędy. Może nawet uda się uniknąć debuggera?
  - `pip install better_exceptions`
  - `export BETTER_EXCEPTIONS=1`
2. [pipsi](https://github.com/mitsuhiko/pipsi)
  - Jest wiele metod instalacji narzędzi napisanych w Pythonie. Co jedna to gorsza.
  - [AWS CLI jest idealnym przykładem.](https://github.com/aws/aws-cli#installation)
  - Ułatwia instalację narzędzi z PyPi.
  - Tworzy virtualenva i dodaje program do PATH, my nie musimy o niczym myśleć.
  - Stworzone przez Armina Ronachera - twórcę Flaska.
  - Projekt porzucony w 2018 - autor teraz zajmuje się głównie Rustem.
3. [pipx](https://github.com/pipxproject/pipx)
  - Następca pipsi - mniej bugów, więcej funkcjonalności.
  - Przede wszystkim działa. Pipsi ma problemy nawet z instalacją.
  - `pipx list`
  - `pipx upgrade-all`
  - `pipx run cowsay`
  - `pipx install black --spec git+https://github.com/ambv/black.git`
  - isort ma nowy release! Ale nie wspomnieli o pyproject.toml...
4. [pre-commit](https://github.com/pre-commit/pre-commit)
  - `pipx install pre-commit`
  - Wygodne zarządzanie gitowymi hookami.
  - Popularne narzędzie, łatwo znaleźć gotowe hooki.
  - Prosta konfiguracja.
  - Można wskazać hooki dostępne np. na GitHubie, można je również wskazać lokalnie.
  - [Przykład w moim repozytorium na GitHubie.](https://github.com/landmaj/py-commit-hooks)
  - Nie musimy przejmować się wersjami Pythona - trzeba je tylko mieć zainstalowane.
  - `pre-commit install`
  - `pre-commit run --all-files`
  - Łatwa integracja z File Watcherami w PyCharmie.
5. [grip](https://github.com/joeyespo/grip)
  - `pipx install grip`
  - `grip gildia.md`
  - Pozwala zobaczyć lokalnie Markdown zanim się go wypchnie do mistrza.
  - Niestety działa tylko z GitHubem.
  - Nie polecam proszenia GitHuba o wyrenderowanie wewnętrznej dokumentacji.
  - GitLab ma bardzo podbne API - ta funkcjonalność się pojawi.
6. [tldr](https://github.com/tldr-pages/tldr)
  - Lepsze man pages jeśli potrzebujesz podstawowej funkcjonalności.
  - `pipx install tldr`
  - `man tar`
  - `tldr tar`
7. [autojump](https://github.com/wting/autojump)
  - Zapomnij o `cd` - da się wygodniej.
  - `sudo apt install autojump`
  - `echo ". /usr/share/autojump/autojump.sh" >> ${HOME}/.bashrc"`

