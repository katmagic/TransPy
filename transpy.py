#!/usr/bin/env python
"""Better internationalization."""

from __future__ import unicode_literals
import yaml

class TranslationError(Exception):
	pass

class InternationalizedString(object):
	"""
	intstr = InternationalizedString(
		en_US="This is the string in American English.",
		es_GB="This is the string in British English."
	)

	intstr.en_US # "This is the string in American English."
	instr['en_GB'] # "This is the string in British English."
	"""

	def __init__(self, internationalizer, **translations):
		self.translations = translations
		self.internationalizer = internationalizer

	def __getitem__(self, language):
		if language in self.translations:
			return self.translations[language]
		else:
			raise TranslationError(
				"We don't have support for this string in %s." % language
			)
	__getattr__ = __getitem__

	def __str__(self):
		return self[self.internationalizer.default_lang]

class Internationalizer(object):
	"""Simply __call__() an Internationalizer instance to return an
	InternationalizedString instance."""

	def __init__(self, trans_file='translations', orig_lang="en_US",
	             default_lang="en_US"):
		self.default_lang = default_lang
		self.orig_lang = orig_lang
		self.translations = yaml.safe_load( open(trans_file).read() )

	def __call__(self, i18n_str):
		"""Return an InternationalizedString instance."""

		if i18n_str in self.translations:
			translations = self.translations[i18n_str]
			if self.default_lang not in translations:
				translations[default_lang] = i18n_str

			return InternationalizedString(self, **translations)
		else:
			raise TranslationError("We don't have a translation for %r." % i18n_str)
