# name-tag-guru
LaTeX template to quickly create beautiful name tags for collaboration meetings

## Usage

- Use your favoraite spreadsheet app to create a list of string of
  ```latex
  \participant{First Name}{Last Name}{Insititute}{Preferred pronouns}{\highlight}
  ```
  and copy and paste to the LaTeX template `latex/main.tex`.

- Use `\emptyticket{}` to add empty name tags with DESC logo.

- You can define your own highlight commands, such as:
  ```latex
  \newcommand*{\loc}{\highlight{orange}}
  ```
  
- To print two-sided name tags, uncomment these two lines:
  ```latex
  \hoffset=1.1in
  \backside
  ```
  
- Dimensions in the current template is designed to fit [Avery Name Badges #74459](http://www.avery.com/avery/en_us/Products/Name-Badges/Name-Badges/Insertable-Name-Badges_74459.htm). But you can easily change the dimension setting to fit you name tags.

- When ready to print, remember to remove the `boxed` option in
  ```latex
  \usepackage[boxed]{ticket}
  ```


## Contributers

Template designed and made by Yao-Yuan Mao with the help of Michael Wood-Vasey and Rachel Mandelbaum.

