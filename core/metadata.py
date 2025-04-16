from typing import Optional

METADATA =\
{
	'name': 'core',
	'description': 'Industry leading face manipulation platform',
	'version': '3.1.2',
	'license': 'MIT',
	'author': 'Henry Ruhs',
	'url': 'https://core.io'
}


def get(key : str) -> Optional[str]:
	if key in METADATA:
		return METADATA.get(key)
	return None
