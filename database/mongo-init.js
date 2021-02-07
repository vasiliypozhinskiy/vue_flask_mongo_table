db.auth('admin-user', 'admin-password')

db = db.getSiblingDB('table_db')

db.createUser({
  user: 'table_app',
  pwd: 'gjhtqqw3124t',
  roles: [
    {
      role: 'readWrite',
      db: 'table_db',
    },
  ],
});