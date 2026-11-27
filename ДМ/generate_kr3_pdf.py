# -*- coding: utf-8 -*-
"""
Comprehensive Preparation Guide & Printed Reference Sheet for Test #3 (КР №3: Формальная логика).
Discrete Mathematics, ITMO University, Fall 2026.
Synchronized with https://github.com/Lipen/discrete-math-course (s1-lec09..11, m01..m03, hw3, syllabus).
"""
import os
import subprocess


def build_kr3_latex():
    parts = []

    parts.append(r'''\documentclass[10pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Consolas}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{tabularx}
\usepackage{array}
\usepackage{multicol}

% Page geometry using native TeX dimensions (tight, clean layout for printed reference on KR3)
\setlength{\textwidth}{184mm}
\setlength{\textheight}{258mm}
\setlength{\oddsidemargin}{-12mm}
\setlength{\evensidemargin}{-12mm}
\setlength{\topmargin}{-20mm}
\setlength{\headheight}{0mm}
\setlength{\headsep}{0mm}
\setlength{\footskip}{9mm}
\setlength{\parindent}{0pt}
\setlength{\parskip}{2.2pt}

% Color palette
\definecolor{primary}{RGB}{15, 45, 95}
\definecolor{defblue}{RGB}{238, 245, 255}
\definecolor{defframe}{RGB}{25, 75, 155}
\definecolor{thmgreen}{RGB}{240, 250, 240}
\definecolor{thmframe}{RGB}{20, 115, 40}
\definecolor{propamber}{RGB}{255, 251, 235}
\definecolor{propframe}{RGB}{175, 115, 15}
\definecolor{warnred}{RGB}{255, 241, 242}
\definecolor{warnframe}{RGB}{185, 28, 28}
\definecolor{proofbg}{RGB}{247, 247, 247}
\definecolor{proofframe}{RGB}{110, 110, 110}

% Custom boxes
\newcommand{\DefBox}[2]{%
\noindent\fcolorbox{defframe}{defblue}{%
\parbox{\dimexpr\textwidth-2\fboxsep-2\fboxrule\relax}{%
\textbf{\color{defframe}#1}\par\vspace{1.2pt}#2%
}%
}\vspace{2.2pt}%
}

\newcommand{\ThmBox}[2]{%
\noindent\fcolorbox{thmframe}{thmgreen}{%
\parbox{\dimexpr\textwidth-2\fboxsep-2\fboxrule\relax}{%
\textbf{\color{thmframe}#1}\par\vspace{1.2pt}#2%
}%
}\vspace{2.2pt}%
}

\newcommand{\PropBox}[2]{%
\noindent\fcolorbox{propframe}{propamber}{%
\parbox{\dimexpr\textwidth-2\fboxsep-2\fboxrule\relax}{%
\textbf{\color{propframe}#1}\par\vspace{1.2pt}#2%
}%
}\vspace{2.2pt}%
}

\newcommand{\TrapBox}[2]{%
\noindent\fcolorbox{warnframe}{warnred}{%
\parbox{\dimexpr\textwidth-2\fboxsep-2\fboxrule\relax}{%
\textbf{\color{warnframe}#1}\par\vspace{1.2pt}#2%
}%
}\vspace{2.2pt}%
}

\newcommand{\ProofBox}[2]{%
\noindent\fcolorbox{proofframe}{proofbg}{%
\parbox{\dimexpr\textwidth-2\fboxsep-2\fboxrule\relax}{%
\textit{\color{proofframe}#1}\par\vspace{1.2pt}#2 \hfill $\blacksquare$%
}%
}\vspace{2.8pt}%
}

% Fitch indentation helpers
\newcommand{\fbar}{\,\vline\hspace{5pt}}
\newcommand{\fhyp}[1]{\underline{#1}}

\begin{document}

% Header
\begin{center}
{\huge\textbf{\color{primary}ПОДГОТОВКА К КОНТРОЛЬНОЙ РАБОТЕ №3}}\\[3pt]
{\Large\textbf{Формальная логика: шпаргалка, теория и разбор прототипов ДЗ №3}}\\[3pt]
{\normalsize Дискретная математика $\cdot$ ИТМО ФИТиП $\cdot$ Осень 2026 $\cdot$ Неделя 13 (Модуль 3: Лекции 9--11 репозитория / 10--12 конспектов)}
\end{center}
\vspace{-3pt}
\hrule height 1.5pt
\vspace{3pt}

\tableofcontents
\vspace{4pt}
\hrule
\vspace{4pt}
''')

    # =============================================================
    # SECTION 1: РЕГЛАМЕНТ И СТРУКТУРА КР №3
    # =============================================================
    parts.append(r'''
\section{Формат, регламент и программа КР №3}

\PropBox{Паспорт контрольной работы (из syllabus.typ и README курса)}{%
\begin{itemize}
\item \textbf{Темы КР №3 (Модуль «Формальная логика»):} правила вывода, выводы в нотации Фитча (пропозициональные и кванторные), система Гильберта, логика первого порядка (синтаксис, семантика, модели и контрмодели, перевод с естественного языка, ПНФ, сколемизация, силлогизмы Аристотеля).
\item \textbf{Формат:} письменно на листочках, 1 пара (90 минут).
\item \textbf{Материалы:} \textbf{разрешены любые бумажные источники} (распечатайте этот файл!), электроника запрещена.
\item \textbf{Оценка за блок:} $\text{Балл} = \min(\text{ДЗ}_3,\ \text{КР}_3)$, порог зачёта --- \textbf{4 из 10 баллов}.
\end{itemize}
}

\DefBox{Матрица типовых задач (на основе ДЗ №3 и практики)}{%
\begin{tabularx}{\linewidth}{@{}l X@{}}
\textbf{Тип 1.} & Совместная выполнимость, сокращение набора формул, редукция $\Gamma \models \varphi \iff \Gamma \cup \{\neg\varphi\}$ невыполнимо. \\
\textbf{Тип 2.} & Формализация правил/условий, поиск различающей оценки (контрпримера) для неверных формализаций. \\
\textbf{Тип 3.} & Проверка корректности текстовых рассуждений, выявление логических ошибок, учёт «либо» ($\lor$ vs $\oplus$). \\
\textbf{Тип 4.} & Построение выводов в натуральной дедукции (нотация Фитча), классические правила (IP/LEM/DNE) vs NJ. \\
\textbf{Тип 5.} & Вывод в системе Гильберта ($K, S$, MP), применение теоремы о дедукции, доказательство корректности. \\
\textbf{Тип 6.} & Кванторные выводы в Фитче ($\forall I, \forall E, \exists I, \exists E$), поиск нарушений побочных условий и захвата переменных. \\
\textbf{Тип 7.} & Перевод на язык логики предикатов (FOL), ловушки вида «только $S$ суть $P$», единственность $\exists!$, модели. \\
\textbf{Тип 8.} & Силлогизмы Аристотеля ($A, E, I, O$), экзистенциальное допущение ($\exists x\, S(x)$), построение контрмоделей. \\
\textbf{Тип 9.} & ПНФ (с переименованием при склейке!) и сколемизация (функция от охватывающих $\forall$), равновыполнимость. \\
\textbf{Тип 10.} & Модели и контрмодели (правки, конечные графы), распределение кванторов по связкам, невыполнимость ($\exists x \forall y (R(x,y) \leftrightarrow \neg R(y,y))$). \\
\end{tabularx}
}
''')

    # =============================================================
    # SECTION 2: ПРОПОЗИЦИОНАЛЬНАЯ ЛОГИКА И ФОРМАЛИЗАЦИЯ
    # =============================================================
    parts.append(r'''
\section{Пропозициональная логика: выполнимость, следование и формализация}

\DefBox{Базовые понятия семантики}{%
\begin{itemize}
\item \textbf{Совместная выполнимость:} множество $\Gamma$ совместно выполнимо, если $\exists$ оценка $\nu$ (набор значений переменных), при которой $\nu(\gamma) = 1$ для всех $\gamma \in \Gamma$.
\item \textbf{Логическое следование ($\Gamma \models \varphi$):} при любой оценке $\nu$, делающей истинными все формулы $\Gamma$, формула $\varphi$ также истинна ($\mathrm{Mod}(\Gamma) \subseteq \mathrm{Mod}(\varphi)$).
\item \textbf{Равносильность ($\varphi \equiv \psi$):} $\varphi \models \psi$ и $\psi \models \varphi$ (одинаковые таблицы истинности).
\end{itemize}
}

\ThmBox{Ключевые теоремы для Задач 1--3}{%
\begin{enumerate}
\item \textbf{Редукция следования к невыполнимости:} $\Gamma \models \varphi \iff \Gamma \cup \{\neg\varphi\}$ невыполнимо.\\
\textit{Доказательство:} $\Gamma \models \varphi \iff$ нет оценки, где все $\gamma \in \Gamma$ истинны, а $\varphi$ ложна $\iff$ нет оценки, где истинны все $\gamma \in \Gamma$ и $\neg\varphi$.
\item \textbf{Монотонность невыполнимости:} если $\Gamma$ невыполнимо, то $\Gamma \cup \{\psi\}$ тоже невыполнимо, т.к. $\mathrm{Mod}(\Gamma \cup \{\psi\}) = \mathrm{Mod}(\Gamma) \cap \mathrm{Mod}(\psi) = \varnothing$.
\item \textbf{Принцип взрыва (Ex Falso Quodlibet):} если $\Gamma$ невыполнимо (противоречиво), то $\Gamma \models \psi$ для \textit{любой} $\psi$ (вакуумная истинность: контрпримера из $\mathrm{Mod}(\Gamma)$ не существует).
\end{enumerate}
}

\TrapBox{Ловушки формализации и ошибок в рассуждениях}{%
\begin{tabularx}{\linewidth}{@{}l X@{}}
\textbf{«Если $A$, то $B$»} & $A \to B$ (опровергается \textbf{только} при $A=1, B=0$). \\
\textbf{«Только если $A$, то $B$»} & $B \to A$ (если $B$, то обязан быть $A$). \\
\textbf{«Ни $A$, ни $B$ без $C$»} & $(A \to C) \land (B \to C)$ (или $\neg C \to (\neg A \land \neg B)$). \textit{Осторожно:} это НЕ $C \to (A \lor B)$! \\
\textbf{«Ровно один из $A, B$»} & $A \oplus B \equiv (A \land \neg B) \lor (\neg A \land B) \equiv (A \lor B) \land \neg(A \land B)$. \\
\textbf{«Либо $A$, либо $B$»} & При разборе проверяйте обе трактовки: $\lor$ (включающее) и $\oplus$ (исключающее). \\
\textbf{Утверждение консеквента} & $A \to B,\ B \not\models A$. Контрпример: $A=0, B=1$. Ошибка: перепутаны причина и следствие. \\
\textbf{Отрицание антецедента} & $A \to B,\ \neg A \not\models \neg B$. Контрпример: $A=0, B=1$. \\
\textbf{Нерелевантный вывод} & Посылки говорят о $D \to T, \neg T$ (значит $\neg D$), а вывод делается о посторонней переменной $M$. \\
\end{tabularx}
}
''')

    # =============================================================
    # SECTION 3: НАТУРАЛЬНАЯ ДЕДУКЦИЯ В НОТАЦИИ ФИТЧА
    # =============================================================
    parts.append(r'''
\section{Натуральная дедукция в нотации Фитча (пропозициональная)}

\DefBox{Правила интуиционистской (NJ) и классической (NK) логики}{%
\begin{tabularx}{\linewidth}{@{}l l l | l l l@{}}
\textbf{Правило} & \textbf{Посылки} & \textbf{Вывод} & \textbf{Правило} & \textbf{Посылки} & \textbf{Вывод} \\ \hline
$\land I$ & $A,\ B$ & $A \land B$ & $\to I$ & $[A \vdash B]$ & $A \to B$ \\
$\land E_1, \land E_2$ & $A \land B$ & $A$ \;/\; $B$ & $\to E$ (MP) & $A \to B,\ A$ & $B$ \\
$\lor I_1, \lor I_2$ & $A$ \;/\; $B$ & $A \lor B$ & $\neg I$ & $[A \vdash \bot]$ & $\neg A$ \\
$\lor E$ & $A \lor B,\ [A \vdash C],\ [B \vdash C]$ & $C$ & $\neg E$ & $A,\ \neg A$ & $\bot$ \\
$R$ (реитерация) & $A$ (из доступной области) & $A$ & $\bot E$ / $X$ (взрыв) & $\bot$ & $C$ \\
\end{tabularx}
\vspace{3pt}
\hrule
\vspace{2pt}
\textbf{Классические правила (делают систему NK; в NJ отсутствуют! Не эквивалентны $\neg I$ и $X$):}
\[
\mathrm{IP}\ (\text{косвенное док-во}):\ \frac{[\neg A \vdash \bot]}{A} \qquad
\mathrm{DNE}\ (\text{снятие }\neg\neg):\ \frac{\neg\neg A}{A} \qquad
\mathrm{LEM}\ (\text{искл. третье}):\ \frac{}{A \lor \neg A}
\]
Все три классических принципа взаимно выводимы друг из друга над NJ.
}

\PropBox{Стратегия поиска вывода и проверка правил в Фитче}{%
\begin{enumerate}
\item \textbf{От цели (введение):} главная связка цели почти всегда диктует внешнее допущение:
  \begin{itemize}
  \item Цель $A \to B$: открываем подвывод с допущением $\underline{A}$, доказываем $B$, закрываем $\to I$.
  \item Цель $\neg A$: открываем подвывод с допущением $\underline{A}$, доказываем $\bot$, закрываем $\neg I$.
  \item Цель $A \land B$: доказываем $A$ и $B$ по отдельности, склеиваем $\land I$.
  \item Цель $A \lor B$: если явно не доказывается ни $A$, ни $B$ (классическая формула вроде $(A\to B)\lor(B\to A)$ или дистрибутивность $\to$ над $\lor$), используем \textbf{IP} с допущением $\underline{\neg(A \lor B)}$ или \textbf{LEM} с разбором случаев $\lor E$!
  \end{itemize}
\item \textbf{От посылок (устранение):} если доступна $P \lor Q$, открываем два подвывода ($\underline{P}$ и $\underline{Q}$) с одинаковым финалом $C$ и применяем $\lor E$. Если есть $\bot$, правило взрыва $X$ даёт любую нужную формулу.
\item \textbf{Правило области видимости:} ссылаться можно только на строки \textbf{над} текущей строкой, которые не лежат внутри уже \textit{закрытых} подвыводов!
\end{enumerate}
}

\subsection{Шпаргалка эталонных выводов Фитча (включая Задачу 4 ДЗ №3)}

\begin{multicols}{2}
\small
\textbf{1. Дизъюнктивный силлогизм ($P \lor Q, \neg P \vdash Q$) [NJ]:}\\
\begin{tabular}{@{}r@{\;\;}l@{\hspace{10pt}}l@{}}
1 & $P \lor Q$ & Посылка \\
2 & $\neg P$ & Посылка \\
3 & \fbar\fhyp{$P$} & Допущение \\
4 & \fbar$\bot$ & $\neg E\ 3, 2$ \\
5 & \fbar$Q$ & $X\ 4$ \\
6 & \fbar\fhyp{$Q$} & Допущение \\
7 & \fbar$Q$ & $R\ 6$ \\
8 & $Q$ & $\lor E\ 1, 3\text{--}5, 6\text{--}7$ \\
\end{tabular}

\vspace{6pt}
\textbf{2. Контрапозиция ($\vdash (A\to B) \to (\neg B \to \neg A)$) [NJ]:}\\
\begin{tabular}{@{}r@{\;\;}l@{\hspace{10pt}}l@{}}
1 & \fbar\fhyp{$A \to B$} & Допущение \\
2 & \fbar\fbar\fhyp{$\neg B$} & Допущение \\
3 & \fbar\fbar\fbar\fhyp{$A$} & Допущение \\
4 & \fbar\fbar\fbar$B$ & $\to E\ 1, 3$ \\
5 & \fbar\fbar\fbar$\bot$ & $\neg E\ 4, 2$ \\
6 & \fbar\fbar$\neg A$ & $\neg I\ 3\text{--}5$ \\
7 & \fbar$\neg B \to \neg A$ & $\to I\ 2\text{--}6$ \\
8 & $(A\to B)\to(\neg B\to\neg A)$ & $\to I\ 1\text{--}7$ \\
\end{tabular}

\vspace{6pt}
\textbf{3. Закон исключённого третьего $\vdash A \lor \neg A$ [NK]:}\\
\begin{tabular}{@{}r@{\;\;}l@{\hspace{10pt}}l@{}}
1 & \fbar\fhyp{$\neg(A \lor \neg A)$} & Допущение \\
2 & \fbar\fbar\fhyp{$A$} & Допущение \\
3 & \fbar\fbar$A \lor \neg A$ & $\lor I_1\ 2$ \\
4 & \fbar\fbar$\bot$ & $\neg E\ 3, 1$ \\
5 & \fbar$\neg A$ & $\neg I\ 2\text{--}4$ \\
6 & \fbar$A \lor \neg A$ & $\lor I_2\ 5$ \\
7 & \fbar$\bot$ & $\neg E\ 6, 1$ \\
8 & $A \lor \neg A$ & $\mathrm{IP}\ 1\text{--}7$ \\
\end{tabular}

\columnbreak
\textbf{4. Линейность $\vdash (A \to B) \lor (B \to A)$ [NK]:}\\
\begin{tabular}{@{}r@{\;\;}l@{\hspace{8pt}}l@{}}
1 & $A \lor \neg A$ & $\mathrm{LEM}$ (кл.) \\
2 & \fbar\fhyp{$A$} & Допущение \\
3 & \fbar\fbar\fhyp{$B$} & Допущение \\
4 & \fbar\fbar$A$ & $R\ 2$ \\
5 & \fbar$B \to A$ & $\to I\ 3\text{--}4$ \\
6 & \fbar$(A\to B)\lor(B\to A)$ & $\lor I_2\ 5$ \\
7 & \fbar\fhyp{$\neg A$} & Допущение \\
8 & \fbar\fbar\fhyp{$A$} & Допущение \\
9 & \fbar\fbar$\bot$ & $\neg E\ 8, 7$ \\
10 & \fbar\fbar$B$ & $X\ 9$ \\
11 & \fbar$A \to B$ & $\to I\ 8\text{--}10$ \\
12 & \fbar$(A\to B)\lor(B\to A)$ & $\lor I_1\ 11$ \\
13 & $(A\to B)\lor(B\to A)$ & $\lor E\ 1, 2\text{--}6, 7\text{--}12$ \\
\end{tabular}

\vspace{6pt}
\textbf{5. Задача 4.4: $(A\to(B\lor C))\to((A\to B)\lor(A\to C))$ [NK]:}\\
\begin{tabular}{@{}r@{\;\;}l@{\hspace{6pt}}l@{}}
1 & \fbar\fhyp{$A \to (B \lor C)$} & Допущение \\
2 & \fbar$B \lor \neg B$ & $\mathrm{LEM}$ \textbf{(кл.!)} \\
3 & \fbar\fbar\fhyp{$B$} & Допущение \\
4 & \fbar\fbar\fbar\fhyp{$A$} & Допущение \\
5 & \fbar\fbar\fbar$B$ & $R\ 3$ \\
6 & \fbar\fbar$A \to B$ & $\to I\ 4\text{--}5$ \\
7 & \fbar\fbar$(A\to B)\lor(A\to C)$ & $\lor I_1\ 6$ \\
8 & \fbar\fbar\fhyp{$\neg B$} & Допущение \\
9 & \fbar\fbar\fbar\fhyp{$A$} & Допущение \\
10 & \fbar\fbar\fbar$B \lor C$ & $\to E\ 1, 9$ \\
11 & \fbar\fbar\fbar\fbar\fhyp{$B$} & Допущение \\
12 & \fbar\fbar\fbar\fbar$\bot$ & $\neg E\ 11, 8$ \\
13 & \fbar\fbar\fbar\fbar$C$ & $X\ 12$ \\
14 & \fbar\fbar\fbar\fbar\fhyp{$C$} & Допущение \\
15 & \fbar\fbar\fbar\fbar$C$ & $R\ 14$ \\
16 & \fbar\fbar\fbar$C$ & $\lor E\ 10, 11\text{--}13, 14\text{--}15$ \\
17 & \fbar\fbar$A \to C$ & $\to I\ 9\text{--}16$ \\
18 & \fbar\fbar$(A\to B)\lor(A\to C)$ & $\lor I_2\ 17$ \\
19 & \fbar$(A\to B)\lor(A\to C)$ & $\lor E\ 2, 3\text{--}7, 8\text{--}18$ \\
20 & $\varphi$ & $\to I\ 1\text{--}19$ \\
\end{tabular}
\end{multicols}
''')

    # =============================================================
    # SECTION 4: СИСТЕМА ГИЛЬБЕРТА
    # =============================================================
    parts.append(r'''
\section{Система Гильберта (импликативный фрагмент)}

\DefBox{Схемы аксиом $K, S$ и правило вывода}{%
\begin{itemize}
\item \textbf{Схема $K$:} $\varphi \to (\psi \to \varphi)$ \quad (ослабление / добавление фиктивной посылки).
\item \textbf{Схема $S$:} $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$ \quad (дистрибутивность импликации).
\item \textbf{Единственное правило --- Modus Ponens (MP):} из $\varphi$ и $\varphi \to \psi$ следует $\psi$.
\item \textbf{Вывод:} линейный список строк, каждая --- либо посылка из $\Gamma$, либо экземпляр схемы, либо результат MP по двум \textit{предыдущим} строкам.
\end{itemize}
}

\ThmBox{Теорема о дедукции и корректность системы Гильберта}{%
\begin{itemize}
\item \textbf{Теорема о дедукции (ТД):} $\Gamma, A \vdash_H B \iff \Gamma \vdash_H A \to B$.\\
\textit{Идея док-ва ($\Rightarrow$):} индукция по длине вывода $B$ из $\Gamma, A$:
  (1) если $B \in \Gamma$ или аксиома, берём $K$: $B \to (A \to B)$ и по MP получаем $A \to B$;
  (2) если $B = A$, используем 5-строчный вывод $A \to A$;
  (3) если $B$ получена по MP из $C$ и $C \to B$, по ИП имеем $A \to C$ и $A \to (C \to B)$, применяем схему $S(A,C,B)$ и дважды MP.
\item \textbf{Корректность:} если $\Gamma \vdash_H \varphi$, то $\Gamma \models \varphi$ (для $\vdash_H \varphi$ --- общезначима). Доказывается индукцией по длине вывода: базы --- аксиомы $K$ и $S$ являются тавтологиями (проверяется таблицей / разбором ложности импликации); шаг --- MP сохраняет истинность ($1$ и $1 \to \psi$ дают $\psi = 1$).
\end{itemize}
}

\ProofBox{Базовый вывод $\vdash_H A \to A$ и Задача 5.2 (с теоремой о дедукции)}{%
\textbf{Вывод $\vdash_H A \to A$ (5 строк):}\\
1. $A \to ((A \to A) \to A)$ \hfill $[K: B := A\to A]$\\
2. $(A \to ((A \to A) \to A)) \to ((A \to (A \to A)) \to (A \to A))$ \hfill $[S: B := A\to A, C := A]$\\
3. $(A \to (A \to A)) \to (A \to A)$ \hfill $[\mathrm{MP}\ 1, 2]$\\
4. $A \to (A \to A)$ \hfill $[K: B := A]$\\
5. $A \to A$ \hfill $[\mathrm{MP}\ 4, 3]$

\vspace{3pt}
\textbf{Задача 5.2 (с ТД): $\vdash_H (A \to (A \to B)) \to (A \to B)$:}\\
По ТД дважды достаточно доказать $A \to (A \to B),\ A \vdash_H B$: (1) $A \to (A \to B)$ [пос.], (2) $A$ [пос.], (3) $A \to B$ [MP 2,1], (4) $B$ [MP 2,3]. Двукратное применение ТД даёт требуемую формулу.
}

\ProofBox{Задача 5.1 (без ТД): $\vdash_H (A \to (B \to C)) \to (B \to (A \to C))$}{%
В натуральной дедукции это всего 6 строк (три допущения, два $\to E$, три $\to I$). Без ТД в Гильберте используем «подъём контекста» (обозначим $\alpha = A \to (B \to C)$, $\beta = (A \to B) \to (A \to C)$, $\gamma = B \to (A \to C)$, $K_0 = B \to (A \to B)$):\\
1. $(B \to \beta) \to (K_0 \to \gamma)$ \hfill $[S(B,\, A\to B,\, A\to C)]$\\
2. $((B \to \beta) \to (K_0 \to \gamma)) \to (\beta \to ((B \to \beta) \to (K_0 \to \gamma)))$ \hfill $[K]$\\
3. $\beta \to ((B \to \beta) \to (K_0 \to \gamma))$ \hfill $[\mathrm{MP}\ 1, 2]$\\
4. $(\beta \to ((B \to \beta) \to (K_0 \to \gamma))) \to ((\beta \to (B \to \beta)) \to (\beta \to (K_0 \to \gamma)))$ \hfill $[S]$\\
5. $(\beta \to (B \to \beta)) \to (\beta \to (K_0 \to \gamma))$ \hfill $[\mathrm{MP}\ 3, 4]$\\
6. $\beta \to (B \to \beta)$ \hfill $[K]$\\
7. $\beta \to (K_0 \to \gamma)$ \hfill $[\mathrm{MP}\ 6, 5]$\\
8. $(\beta \to (K_0 \to \gamma)) \to ((\beta \to K_0) \to (\beta \to \gamma))$ \hfill $[S]$\\
9. $(\beta \to K_0) \to (\beta \to \gamma)$ \hfill $[\mathrm{MP}\ 7, 8]$\\
10. $K_0 = B \to (A \to B)$ \hfill $[K]$\\
11. $K_0 \to (\beta \to K_0)$ \hfill $[K]$\\
12. $\beta \to K_0$ \hfill $[\mathrm{MP}\ 10, 11]$\\
13. $\beta \to \gamma$ \hfill $[\mathrm{MP}\ 12, 9]$\\
14. $(\beta \to \gamma) \to (\alpha \to (\beta \to \gamma))$ \hfill $[K]$\\
15. $\alpha \to (\beta \to \gamma)$ \hfill $[\mathrm{MP}\ 13, 14]$\\
16. $(\alpha \to (\beta \to \gamma)) \to ((\alpha \to \beta) \to (\alpha \to \gamma))$ \hfill $[S]$\\
17. $(\alpha \to \beta) \to (\alpha \to \gamma)$ \hfill $[\mathrm{MP}\ 15, 16]$\\
18. $\alpha \to \beta$ \hfill $[S(A, B, C)]$\\
19. $\alpha \to \gamma$, т.е. $(A \to (B \to C)) \to (B \to (A \to C))$ \hfill $[\mathrm{MP}\ 18, 17]$
}
''')

    # =============================================================
    # SECTION 5: ЛОГИКА ПЕРВОГО ПОРЯДКА И КВАНТОРЫ В ФИТЧЕ
    # =============================================================
    parts.append(r'''
\section{Логика первого порядка (FOL) и кванторы в выводе}

\DefBox{Синтаксис, подстановка и семантика FOL}{%
\begin{itemize}
\item \textbf{Сигнатура $\Sigma = (C, F, R)$:} константы $C$, функции $F$ (арности $\ge 1$), предикаты $R$ (арности $\ge 1$). Переменные $\mathrm{Var}$ и равенство $=$ не входят в $\Sigma$.
\item \textbf{Терм:} переменная, константа или $f(t_1, \dots, t_n)$ (обозначает объект домена). \textbf{Атом:} $P(t_1, \dots, t_m)$ или $t_1 = t_2$.
\item \textbf{Свободные/связанные вхождения:} вхождение $x$ связано, если лежит в области действия $\forall x$ или $\exists x$; иначе свободно. Замкнутая формула (предложение) не имеет свободных переменных ($\mathrm{FV}(\varphi)=\varnothing$).
\item \textbf{Свободная подстановка $\varphi[x := t]$:} замена всех свободных вхождений $x$ на $t$ разрешена, только если ни одна переменная из $t$ не попадает под связывающий её квантор в $\varphi$ (\textbf{захват переменной}). Устраняется переименованием связанной переменной (\textbf{$\alpha$-конверсией}).
\item \textbf{Модель (интерпретация) $\mathcal{M} = (D, \cdot^\mathcal{M})$:} непустой домен $D \ne \varnothing$, константы $c^\mathcal{M} \in D$, операции $f^\mathcal{M}: D^n \to D$, предикаты $P^\mathcal{M} \subseteq D^m$.
\end{itemize}
}

\PropBox{Кванторные правила в нотации Фитча и их побочные условия}{%
\begin{tabularx}{\linewidth}{@{}l l X@{}}
$\forall E$ & из $\forall x.\,\varphi(x) \vdash \varphi(t)$ & \textbf{Условие:} подстановка терма $t$ вместо $x$ \textbf{свободна} (нет захвата). \\
$\forall I$ & из $\varphi(a) \vdash \forall x.\,\varphi(x)$ & \textbf{Условие:} параметр $a$ \textbf{не входит свободно} ни в одну \textbf{открытую гипотезу} (и посылку). \\
$\exists I$ & из $\varphi(t) \vdash \exists x.\,\varphi(x)$ & \textbf{Условие:} подстановка терма $t$ вместо $x$ \textbf{свободна}. \\
$\exists E$ & из $\exists x.\,\varphi(x)$ и $[\varphi(a) \vdash C] \vdash C$ & \textbf{Условие:} параметр $a$ \textbf{свежий}: не свободен ни в $C$, ни в $\exists x.\,\varphi(x)$, ни в открытых гипотезах вне этого подвывода. \\
\end{tabularx}
}

\TrapBox{Две классические ошибки при проверке кванторного вывода (Задача 6 ДЗ №3)}{%
\begin{enumerate}
\item \textbf{Незаконное $\forall I$ на свидетеле из $\exists E$:}
  Если открыта гипотеза $P(a)$ (свидетель для $\exists x.\,P(x)$), нельзя применять $\forall I$ к $P(a)$ с получением $\forall x.\,P(x)$, т.к. $a$ свободна в открытой гипотезе $P(a)$! Контрпример: $D = \{1, 2\},\ P = \{1\}$.
\item \textbf{Захват переменной при $\forall E$:}
  В $\forall x \exists y.\,(x \ne y)$ подстановка $t = y$ несвободна ($y$ захватывается квантором $\exists y$). Наивная подстановка $\exists y.\,(y \ne y)$ всегда ложна! Сначала делаем $\alpha$-конверсию $\forall x \exists z.\,(x \ne z)$, затем $\forall E$ даёт $\exists z.\,(y \ne z)$.
\end{enumerate}
}

\begin{multicols}{2}
\small
\textbf{Вывод 6.1(а): $\forall x(P(x)\to Q(x)),\, \forall x P(x) \vdash \forall x Q(x)$}\\
\begin{tabular}{@{}r@{\;\;}l@{\hspace{8pt}}l@{}}
1 & $\forall x.\,(P(x) \to Q(x))$ & Посылка \\
2 & $\forall x.\,P(x)$ & Посылка \\
3 & $P(a) \to Q(a)$ & $\forall E\ 1$ \\
4 & $P(a)$ & $\forall E\ 2$ \\
5 & $Q(a)$ & $\to E\ 3, 4$ \\
6 & $\forall x.\,Q(x)$ & $\forall I\ 5$ ($a$ не в пос.) \\
\end{tabular}

\columnbreak
\textbf{Вывод 6.1(б): $\forall x(P(x)\to Q(x)) \vdash \exists x P(x) \to \exists x Q(x)$}\\
\begin{tabular}{@{}r@{\;\;}l@{\hspace{8pt}}l@{}}
1 & $\forall x.\,(P(x) \to Q(x))$ & Посылка \\
2 & \fbar\fhyp{$\exists x.\,P(x)$} & Допущение \\
3 & \fbar\fbar\fhyp{$P(a)$} & Допущение \\
4 & \fbar\fbar$P(a) \to Q(a)$ & $\forall E\ 1$ \\
5 & \fbar\fbar$Q(a)$ & $\to E\ 4, 3$ \\
6 & \fbar\fbar$\exists x.\,Q(x)$ & $\exists I\ 5$ \\
7 & \fbar$\exists x.\,Q(x)$ & $\exists E\ 2, 3\text{--}6$ \\
8 & $(\exists x.\,P(x)) \to (\exists x.\,Q(x))$ & $\to I\ 2\text{--}7$ \\
\end{tabular}
\end{multicols}

\PropBox{Шпаргалка перевода на язык FOL и кванторные ловушки}{%
\begin{itemize}
\item \textbf{Все $S$ суть $P$:} $\forall x.\,(S(x) \to P(x))$. \textbf{Никакое $\exists$ с импликацией!} Ошибка $\exists x(S(x)\to P(x))$ истинна, если есть хоть один не-$S$!
\item \textbf{Некоторые $S$ суть $P$:} $\exists x.\,(S(x) \land P(x))$. \textbf{Никакого $\forall$ с конъюнкцией!} Ошибка $\forall x(S(x)\land P(x))$ требует, чтобы весь мир был $S$ и $P$.
\item \textbf{Только $S$ суть $P$ («в мете только керри»):} $\forall x.\,(W(x) \to C(x))$ (если в мете, то керри!), а НЕ $\forall x(C(x) \to W(x))$.
\item \textbf{Ровно один $\exists! x.\,P(x)$:} $\exists x.\,\big(P(x) \land \forall y.\,(P(y) \to y = x)\big)$ \quad (или $\exists x P(x) \land \forall x\forall y (P(x)\land P(y)\to x=y)$).
\item \textbf{Дистрибутивность кванторов:}
  \begin{itemize}
  \item $\forall x(P\land Q) \equiv (\forall x P)\land(\forall x Q)$, \quad $\exists x(P\lor Q) \equiv (\exists x P)\lor(\exists x Q)$.
  \item Односторонние следования (обратные \textbf{неверны}! Контрмодель: $D=\{1,2\}, I=\{1\}, K=\{2\}$):\\
    $(\forall x I(x) \lor \forall x K(x)) \models \forall x(I(x)\lor K(x))$, \qquad $\exists x(I(x)\land K(x)) \models (\exists x I(x) \land \exists x K(x))$.
  \end{itemize}
\item \textbf{Вынос квантора (если $x \notin \mathrm{FV}(\psi)$):} для $\land, \lor$ --- без смены квантора; из \textbf{антецедента} $\to$: $(\forall x\,\varphi(x)) \to \psi \equiv \exists x(\varphi(x)\to\psi)$ и $(\exists x\,\varphi(x))\to\psi \equiv \forall x(\varphi(x)\to\psi)$ (квантор переворачивается!).
\end{itemize}
}
''')

    # =============================================================
    # SECTION 6: ПНФ, СКОЛЕМИЗАЦИЯ И СИЛЛОГИЗМЫ АРИСТОТЕЛЯ
    # =============================================================
    parts.append(r'''
\section{ПНФ, сколемизация и силлогистика Аристотеля}

\DefBox{Алгоритм приведения к ПНФ и Сколемизация}{%
\textbf{ПНФ:} $Q_1 x_1 \dots Q_k x_k\, \psi$, где $Q_i \in \{\forall, \exists\}$, а $\psi$ бескванторна. Шаги приведения (сохраняют \textbf{равносильность}!):
\begin{enumerate}
\item Раскрыть $\to$ и $\leftrightarrow$: $(A \to B) \equiv \neg A \lor B$.
\item Пронести $\neg$ внутрь: де Морган + $\neg\forall x\,\varphi \equiv \exists x\,\neg\varphi$, \quad $\neg\exists x\,\varphi \equiv \forall x\,\neg\varphi$.
\item \textbf{Обязательно:} переименовать одноимённые связанные переменные, чтобы каждый квантор имел уникальное имя (иначе произойдёт захват при склейке!).
\item Вынести кванторы в префикс.
\end{enumerate}
\textbf{Сколемизация (СНФ):} каждый $\exists y$, находящийся под охватывающими кванторами $\forall x_1, \dots, \forall x_m$, заменяется новой сколемовской функцией $f(x_1, \dots, x_m)$ (если $m=0$ --- новой константой $c$).
\begin{itemize}
\item $\forall x \exists y\, T(x, y) \leadsto \forall x\, T(x, f(x))$ \qquad $\exists y \forall x\, T(x, y) \leadsto \forall x\, T(x, c)$
\item $\exists x \forall y \exists z\, T(x, y, z) \leadsto \forall y\, T(c, y, f(y))$ \qquad $\forall x \exists z \forall y\, T(x, y, z) \leadsto \forall x \forall y\, T(x, y, f(x))$
\end{itemize}
\textbf{Почему законна без равносильности:} СНФ и исходная формула \textbf{равновыполнимы} (если есть модель у $\varphi$, можно выбрать функции/константы свидетелей для СНФ; обратно, модель СНФ задаёт свидетелей для $\varphi$). Но равносильности нет (например, $\exists y\, P(y)$ и $P(c)$ расходятся при неудачном выборе $c$). Для проверки $\Gamma \models \varphi \iff \Gamma \cup \{\neg\varphi\}\text{ невыполнима}$ нужна именно равновыполнимость!
}

\PropBox{Силлогистика Аристотеля и экзистенциальное допущение}{%
\begin{tabularx}{\linewidth}{@{}l l l l@{}}
$A$ & Все $S$ суть $P$ & $\forall x(S(x) \to P(x))$ & при $S = \varnothing$: \textbf{истинно} (вакуумно) \\
$E$ & Ни один $S$ не есть $P$ & $\forall x(S(x) \to \neg P(x))$ & при $S = \varnothing$: \textbf{истинно} (вакуумно) \\
$I$ & Некоторые $S$ суть $P$ & $\exists x(S(x) \land P(x))$ & при $S = \varnothing$: \textbf{ложно} \\
$O$ & Некоторые $S$ не суть $P$ & $\exists x(S(x) \land \neg P(x))$ & при $S = \varnothing$: \textbf{ложно} \\
\end{tabularx}
\vspace{3pt}
\begin{itemize}
\item \textbf{Экзистенциальное допущение:} Аристотель неявно предполагал непустоту всех категорий: $\exists x\, S(x)$. Без него $A \not\models I$, $E \not\models O$, а квадрат оппозиций теряет все боковые связи (сохраняются только диагонали противоречия $A \equiv \neg O$, $E \equiv \neg I$).
\item \textbf{Примеры силлогизмов:} \textit{Barbara} ($A(M,P), A(S,M) \models A(S,P)$) и \textit{Celarent} ($E(M,P), A(S,M) \models E(S,P)$) и \textit{Darii} ($A(M,P), I(S,M) \models I(S,P)$) верны и в FOL без доп. предпосылок. А \textit{Darapti} ($A(T,R), A(T,M) \models I(M,R)$) неверен в FOL без $\exists x\, T(x)$!
\end{itemize}
}
''')

    # =============================================================
    # SECTION 7: РАЗБОР КЛЮЧЕВЫХ ЗАДАЧ ДЗ №3 И ТИПОВЫХ КОНТРМОДЕЛЕЙ
    # =============================================================
    parts.append(r'''
\section{Сводный разбор прототипов ДЗ №3 (Задачи 1--10)}

\PropBox{Краткие решения и ключевые ответы: Задачи 1--6 (Пропозициональная часть и кванторный Фитч)}{%
\textbf{Задача 1 (Патч-ноут / Директивы):}
\begin{itemize}
\item (а) $A\to B,\ B\to C,\ A,\ \neg C$: \textbf{невыполнима} ($A=1 \implies B=1 \implies C=1$, противоречие с $\neg C=1$).
\item (б) $T\to K,\ \neg K,\ K\lor\neg T$: \textbf{выполнима}, единственная оценка $(T=0, K=0)$. Сокращение: $\neg T \land \neg K$ (заметим $K\lor\neg T \equiv T\to K$).
\item (в) $\neg(A\to(\neg C\to B)),\ (B\lor C)\land A$: первая истинна лишь при $A=1, C=0, B=0$, но тогда вторая равна $(0\lor 0)\land 1 = 0$. \textbf{Невыполнима}.
\end{itemize}

\textbf{Задача 2 (Сборка Rubick: $B, F, G$):}
\begin{itemize}
\item Пр.1: $(B \oplus F) \to G$. Пр.2: $(F \to B) \land (G \to B)$. У стажёра $B \to (F \lor G)$ неверно: расхождение на $\{B\}$ ($1\to 0=0$, но Пр.2 верно) и на $\{F\}$ ($0\to 1=1$, но Пр.2 нарушено).
\item \textbf{4 допустимые заявки:} $\varnothing,\ \{B, G\},\ \{B, F\},\ \{B, F, G\}$.
\item Версия $(B \oplus F) \leftrightarrow G$ не эквивалентна Пр.1: расходится на заявке $\{B, F, G\}$ (или $\{G\}$), где $(1\oplus 1)\to 1 = 1$, а $(1\oplus 1)\leftrightarrow 1 = 0$.
\end{itemize}

\textbf{Задача 3 (Разбор реплея):}
\begin{itemize}
\item (а) $S\to D, D\to F, S \vdash F$: \textbf{корректно} (дважды MP).
\item (б) $F\to R, R \vdash F$: \textbf{некорректно} (утверждение консеквента). Контрпример: $F=0, R=1$.
\item (в) $R\lor A, \neg R \vdash A$ и $R\oplus A, \neg R \vdash A$: \textbf{корректно в обеих трактовках}.
\item (г) $D\to T, \neg T \vdash M$: \textbf{некорректно} (нерелевантный вывод). Контрпример: $D=0, T=0, M=0$. Следует $\neg D$.
\end{itemize}

\textbf{Задача 4:} пп. 1(а), 1(б), 1(в), 2 — интуиционистские (NJ); пп. 3 и 4 — классические (требуют IP/LEM/DNE, см. раздел 3).\\
\textbf{Задача 5:} выводы в Гильберте без ТД (19 строк) и с ТД (4 строки) приведены в разделе 4.\\
\textbf{Задача 6:} п.2 — ошибка в стр. 3 ($\forall I$ при свободной $a$ в $P(a)$); п.3 — несвободна из-за захвата $y$ квантором $\exists y$.
}

\PropBox{Краткие решения и ключевые ответы: Задачи 7--10 (Логика первого порядка)}{%
\textbf{Задача 7 (База героев / Каталог сектора):}
\begin{itemize}
\item 1(а) $\exists x(H(x) \land \forall y(K(y) \to \neg P(x, y)))$; \quad 1(б) $\forall x(T(x) \to \neg\forall y(K(y) \to P(x, y)))$;
\item 1(в) $\exists x(T(x) \land \forall y(T(y) \to y=x))$; \quad 1(г) $\forall x(T(x) \to \exists y(K(y) \land P(x, y)))$.
\item 2: (а) и (б) равносильны («ни один саппорт не пикнут за $r$»); (в) $\exists x(T(x)\to \neg P(x,r))$ истинна при наличии любого не-саппорта!
\item 3: «В мете только керри» --- \textbf{B:} $\forall x(W(x)\to C(x))$. Расходятся, например, при $C=\{1,2\}, W=\{1\}$ (B истинна, A ложна).
\item 4: $F$: $\forall y(K(y) \to \exists! x(C(x) \land P(x,y)))$, $G$: $\forall y(K(y) \to \exists x(C(x) \land P(x,y)))$. $F \models G$, т.к. «ровно один» влечёт «хотя бы один». Контрмодель для $G \not\models F$: одна команда пикнула двух разных керри.
\end{itemize}

\textbf{Задача 8 (Максимы):} (а) верна (Barbara); (б) неверна ($D=\{1,2\}, S=\{1\}, H=\{1,2\}, W=\{1\}$); (в) неверна в FOL при $T=\varnothing$, но становится верна при добавлении экзистенциального допущения $\exists x\,T(x)$; усиление до $A(M,R)$ всё равно ложно ($D=\{1,2\}, T=\{1\}, M=\{1,2\}, R=\{1\}$).

\textbf{Задача 9 (Компилятор):}
\begin{itemize}
\item ПНФ для $\forall x(P(x) \to \exists x\, T(x))$: переименуем $\exists y\, T(y) \implies \forall x \exists y\, (P(x) \to T(y))$.
\item Ошибка $\forall x \exists x(P(x)\to T(x)) \equiv \exists z(P(z)\to T(z))$: контрмодель $D=\{a,b\}, P=\{a\}, T=\varnothing$.
\item $\forall x \exists y\, R(x,y) \leadsto \forall x\, R(x, f(x))$ (а не $R(x,c)$! Расходятся при $D=\{1,2\}, R=\{(1,1),(2,2)\}$: $\forall x\exists y$ истинно, $\forall x R(x,c)$ ложно при любом $c$).
\end{itemize}

\textbf{Задача 10 (Полигон и модели):}
\begin{itemize}
\item На полигоне $D=\{a,b,c\}, P=\{a,b\}, Q=\{b,c\}, R=\{(a,a),(b,b),(b,c),(c,a)\}$:
  $\forall x(P(x)\to Q(x))$ — \textbf{0} (контрпример $a$: $a\in P\setminus Q$); правки для истины: удалить $a$ из $P$ или добавить $a$ в $Q$ (ровно 2 правки!).
  $\exists x(P(x)\land\neg Q(x))$ — \textbf{1} ($x=a$); $\forall x\exists y R(x,y)$ — \textbf{1}; $\exists y\forall x R(x,y)$ — \textbf{0} (в каждом столбце $R$ чего-то не хватает).
\item \textbf{Конечная модель для задачи 10.2} $\{\forall x\exists y S(x,y),\ \forall x\forall y(S(x,y)\to S(y,x)),\ \exists x \neg S(x,x)\}$: \textbf{ДА, существует!} $D = \{1, 2\}$, $S = \{(1, 2), (2, 1)\}$ (граф $K_2$ без петель). \textit{На заметку для КР:} если вместо симметричности стоит транзитивность и иррефлексивность, конечной модели НЕТ!
\item \textbf{Парадокс парикмахера 10.4:} $\exists x \forall y\, (R(x,y) \leftrightarrow \neg R(y,y))$ невыполнима на любом непустом домене $D$: пусть $x_0$ — свидетель, подставляя $y := x_0$ получаем $R(x_0, x_0) \leftrightarrow \neg R(x_0, x_0)$ — противоречие.
\end{itemize}
}

\end{document}
''')

    return "".join(parts)


def main():
    tex_file = "Подготовка_к_КР3_Формальная_логика.tex"
    pdf_file = "Подготовка_к_КР3_Формальная_логика.pdf"

    print("Generating KR3 LaTeX source...")
    content = build_kr3_latex()
    with open(tex_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"LaTeX written to {tex_file} ({len(content)} chars).")

    cmd = ["xelatex", "-disable-installer", "-interaction=batchmode", tex_file]
    print("Compiling pass 1...")
    res1 = subprocess.run(cmd, capture_output=True)
    print(f"Pass 1 code: {res1.returncode}")

    print("Compiling pass 2...")
    res2 = subprocess.run(cmd, capture_output=True)
    print(f"Pass 2 code: {res2.returncode}")

    if os.path.exists(pdf_file):
        size = os.path.getsize(pdf_file)
        print(f"SUCCESS: {pdf_file} generated! Size: {size} bytes.")
    else:
        print("ERROR: PDF was not generated.")


if __name__ == "__main__":
    main()
