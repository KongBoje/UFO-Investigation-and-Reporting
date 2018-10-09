# UFO-Code Analysis
### Exercise page
- https://datsoftlyngby.github.io/soft2018fall/UFO/02-CodeAnalysis.html

### Exercise 1
I ran the analysis with the following command: "./run.sh pmd -d ~/Documents/NetBeansProjects/Gutenberg-book-project -R category/java/codestyle.xml -f html > ~/pmdresult.html" on this project:
- https://github.com/KongBoje/Gutenberg-book-project

I got the following PMD report on this project with the category being condestyle.xml:
- https://github.com/KongBoje/UFO-LinQ-Investigations/blob/master/files/PMDReport.pdf

I have picked the 10 following checks which I think are important when viewing codestyle in this project:
- **1: OnlyOneReturn** - A method should have only one exit point, and that should be the last statement in the method.
- **2: UnnecessaryConstructor** - This rule detects when a constructor is not necessary; i.e., when there is only one constructor and the constructor is identical to the default constructor. The default constructor should has same access modifier as the declaring class. In an enum type, the default constructor is implicitly private.
- **3: ShortVariable** - Fields, local variables, or parameter names that are very short are not helpful to the reader.
- **4: PrematureDeclaration** - Checks for variables that are defined before they might be used. A reference is deemed to be premature if it is created right before a block of code that doesn’t use it that also has the ability to return or throw an exception.
- **5: ClassNamingConventions** - Configurable naming conventions for type declarations. This rule reports type declarations which do not match the regex that applies to their specific kind (e.g. enum or interface). Each regex can be configured through properties.
By default this rule uses the standard Java naming convention (Pascal case), and reports utility class names not ending with ‘Util’.
- **6: UnnecessaryModifier** - Fields in interfaces and annotations are automatically public static final, and methods are public abstract. Classes, interfaces or annotations nested in an interface or annotation are automatically public static (all nested interfaces and annotations are automatically static). Nested enums are automatically static. For historical reasons, modifiers which are implied by the context are accepted by the compiler, but are superfluous.
- **7: VariableNamingConventions** - A variable naming conventions rule - customize this to your liking. Currently, it checks for final variables that should be fully capitalized and non-final variables that should not include underscores.
- **8: UnnecessaryLocalBeforeReturn** - Avoid the creation of unnecessary local variables.
- **9: IdenticalCatchBranches** - Identical catch branches use up vertical space and increase the complexity of code without adding functionality. It’s better style to collapse identical branches into a single multi-catch branch.
- **10: ConfusingTernary** - Avoid negation within an “if” expression with an “else” clause. For example, rephrase: if (x != y) diff(); else same(); as: if (x == y) same(); else diff();.
Most “if (x != y)” cases without an “else” are often return cases, so consistent use of this rule makes the code easier to read. Also, this resolves trivial ordering problems, such as “does the error case go first?” or “does the common case go first?”.

#### I think all of these 10 checks are important in your code, since they make the code easier to navigate in and also probably slight faster.

### Exercise 2
- Source code link
- Report on profile result and explain what is seen.
- Micro-benchmark if possible
