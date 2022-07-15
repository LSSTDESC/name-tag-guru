# name-tag-guru
LaTeX template to quickly create beautiful name tags (badges) for collaboration meetings

## Preview

You can preview how your badge would look like [on this page](https://lsstdesc.github.io/name-tag-guru/).

## Usage

- Use your favorite spreadsheet app (e.g., Excel) to create a list of string of
  ```latex
  \participant{Large-font Badge Name}{Small-font Badge Name}{Affiliation}{Pronouns}{\command}
  ```
  and copy and paste to the LaTeX template `latex/main.tex`.

  Usually the spreadsheet formula would look like this:
  ```
  = "\participant{" & B1 & "}{" & B2 & "}{" & B3 & "}{" & B4 & "}{\" & B5 & "}"
  ```
  with B1 to B5 being the cells that specify the large- and small-font badge names,
  affiliation, pronouns, and highlighting command.


- Use `\emptyticket{}` to add empty name tags with the background.


- You can define your own highlight commands, such as:
  ```latex
  \newcommand*{\loc}{\highlight{orange}}
  ```

- To include CJK character, uncomment the following two lines. One also needs to compile with `xelatex`. A CJK font is also required (current set to `Noto Sans CJK TC`).
  ```latex
  \usepackage{xeCJK}
  \setCJKmainfont{Noto Sans CJK TC}
  ```


- To print two-sided name tags, uncomment these two lines:
  ```latex
  \hoffset=1.1in
  \backside
  ```


- Dimensions in the current template is designed to fit [Avery Name Badges #74459](http://www.avery.com/avery/en_us/Products/Name-Badges/Name-Badges/Insertable-Name-Badges_74459.htm). But you can easily change the dimension setting to fit you name tags.

  There relevant quantities are:
  - `\hoffset`, `\voffset`: setting page margins;
  - `\ticketSize`, `\ticketDistance`: setting the size of badges and the padding in between (current set in units of 0.01in);
  - `\ticketNumbers`: setting the number of badges per page;
  - the numbers in parentheses after `\put`: setting the location of each element.


- When ready to print, remember to remove the `boxed` option in
  ```latex
  \usepackage[boxed]{ticket}
  ```
  Leave the `boxed` option on to see how the badges would look like.


## Automated badge generation from registration database

We provide a script that can automagically query the registration database from 
the [meetings-registration-form](https://github.com/LSSTDESC/meeting-registration-form)
repository to generate a `participants.tex` file.
To install the `sqlalchemy` requirement:
```
$ pip install sqlalchemy
```
Then copy the secret heroku database URL from the settings tab of the Heroku service 
into a `db_secret` file at the root of this repo. Be careful not to commit or share this
file!
Finally, run the following command at the root of this repo:
```
$ python badges_from_db.py
```
And that's it, you now have a `participants.tex` file in the `latex` folder, ready to be
processed.


## Contributers

This template is designed and implemented by [Yao-Yuan Mao](https://yymao.github.io),
with helpful suggestions contributed by
Alex Kim, Rachel Mandelbaum, Phil Marshall, Anže Slosar, and Michael Wood-Vasey.


