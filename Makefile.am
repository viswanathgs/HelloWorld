## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = src 

helloworlddocdir = ${prefix}/doc/helloworld
helloworlddoc_DATA = \
	README\
	COPYING\
	AUTHORS\
	ChangeLog\
	INSTALL\
	NEWS


EXTRA_DIST = $(helloworlddoc_DATA)


# Remove doc directory on uninstall
uninstall-local:
	-rm -r $(helloworlddocdir)
