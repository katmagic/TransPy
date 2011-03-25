#!/usr/bin/env python
from __future__ import unicode_literals
import transpy
import unittest

class TranslationTest(unittest.TestCase):
	def testTranslation(self):
		i = transpy.Internationalizer('test.trans', default_lang="es")
		i18n_str = i("This is an example.")
		self.assertEqual(
			"¡Hola! Este es un ejemplo.",
			"¡Hola! %s" % i18n_str
		)

		# Try changing the default language.
		i.default_lang = "zh_TW"
		self.assertEqual("這是一個例子。", str(i18n_str))

		# Get non-default languages.
		self.assertEqual("This is an example.", i18n_str.en_US)

		# Try getting a language we don't have a translation for.
		self.assertRaises(
			transpy.TranslationError,
			lambda: str(i("This is an example"))
		)

		# Try getting a translation we don't have any information about.
		self.assertRaises(transpy.TranslationError, i, "x_x")

if __name__ == '__main__':
	unittest.main()
