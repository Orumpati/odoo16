{
    'name': 'School Management',
    'version': '1.1',
    'category': 'management',
    'sequence': 40,
    'summary': 'This is the first module i created in odoo16',
    'author':'sai krishna',
    'depends': ['base'],
  'data': [
 "security/ir.model.access.csv",
  "views/school_view.xml",
  "data/data.xml"
],
 
    'installable': True,
    'application': True,
    

    'license': 'LGPL-3',
}
