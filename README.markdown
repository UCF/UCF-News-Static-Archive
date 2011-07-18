# Instructions
* Run get_archive.sh
	* Relies on wget to make a copy of the archive. WGET has to be run with `-l inf` or else not all of the archive paginations sections are retrieved.
* Create an arbitrary output directory
* Verify that the ARCHIVE_SOURCE_DIR and ARCHIVE_TARGET_DIR constants in clean_archive.py are pointing to the correct location
* Run clean_archive.py
* The static archive is contained in the specified output directory
