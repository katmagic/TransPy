TransPy - Better internationalization
=====================================

TransPy is an internationalization library that doesn't slaughter the
readability of your code, and doesn't cause infinite pain for translators.

Usage
-----

Using TransPy is easy:

	import transpy
	i = transpy.Internationalizer('babble.trans', default_lang='es')

Now all you need to do to create an internationalized string is call i.

	# This will output "¡Hola, mundo!".
	print( i("Hello, world!") )

You can also change the default language at run time, and it will affect all
`InternationalizedString`s initialized from an `Internationalizer`.

	i.default_lang = 'en_US'
	# This will output "Hello, world!".
	print( i("Hello, world!") )

And you can get different languages on a per-string basis, too.

	i("Hello, world!").en_GB # "Hello, world!"
	i("This is an example.")['es'] # "Este es un ejemplo."

If you use a request a string there's no translation for, or you request a
language we have no translation for, a `TranslationError` is raised.

	i("gobledeegook")
	i("Hello, world!")['zh_CN']

Writing Translation Files
-------------------------

The format for translation files is pretty simple. A translation file is just a
YAML document. An example translation file might look something like this.

	"This is an example.":
	  en_US: "This is an example."
	  en_GB: "This is an example."
	  es: "Este es un ejemplo."
	  zh_TW: "這是一個例子。"
	  ar: "وهذا مثال."
	  th: "นี้เป็นตัวอย่าง"

	"This is a second example.":
	  th: "นี่เป็นอีกตัวอย่างหนึ่ง"
	  hy: "Սա եւս մեկ օրինակ."
	  af: "Dit is nog 'n voorbeeld."
	  eu: "Honen beste adibide bat da."
	  sw: "Huu ni mfano mwingine."

The upper level keys ("This is an example." and "This is a second example.") are
the strings one uses in one's program, and the lower-level keys are language
codes. It is important to note is that YAML is sensitive to indentation, and
*does not allow you to use tabs*.

License
-------

This is free and unencumbered software released into the public domain. For more
information, see [unlicense.org](http://unlicense.org).
