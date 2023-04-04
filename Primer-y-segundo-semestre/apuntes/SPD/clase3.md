# Clase 3

## Interaccion con la terminal

```commandline
rodri@laptop-agus MINGW64 ~
$ cd TecnicaturaGit

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ mkdir Readme

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ gt status
bash: gt: command not found

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Python/leccion1/main.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Readme/

no changes added to commit (use "git add" and/or "git commit -a")

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ git add .

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ git commit -m "Actividad realizada en la clase 3"
[master 13fa1fc] Actividad realizada en la clase 3
 2 files changed, 96 insertions(+)
 create mode 100644 Readme/readme.txt

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Readme/readme.txt

no changes added to commit (use "git add" and/or "git commit -a")

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ git commit -am "actualizamos readme.txt"
[master 8520aa3] actualizamos readme.txt
 1 file changed, 4 insertions(+), 1 deletion(-)

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ git checkout -f

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ git add .

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ git restore --staged Readme/readme.txt

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Readme/readme.txt

no changes added to commit (use "git add" and/or "git commit -a")

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ git diff
diff --git a/Readme/readme.txt b/Readme/readme.txt
index 2930a86..7362886 100644
--- a/Readme/readme.txt
+++ b/Readme/readme.txt
@@ -2,4 +2,10 @@ Esta es un practica de clase numero 3 de sistema de procesamientos de datos
 del dia martes 26 de abril

 tambien el dia de hoy commiteamos las actividades laboratorio
-de programacion
\ No newline at end of file
+de programacion
+
+esta es la segunda vez que escribo esto
+ya que me pidieron hacer un git checkout
+
+nuevas lineas
+-------------
\ No newline at end of file

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ git diff -stat
error: did you mean `--stat` (with two dashes)?

rodri@laptop-agus MINGW64 ~/TecnicaturaGit (master)
$ git diff --stat
 Readme/readme.txt | 8 +++++++-
 1 file changed, 7 insertions(+), 1 deletion(-)

```