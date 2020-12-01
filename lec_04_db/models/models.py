from peewee import *

database = SqliteDatabase('../Chinook_Sqlite.sqlite')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Artist(BaseModel):
    artist_id = AutoField(column_name='ArtistId')
    name = UnknownField(column_name='Name', null=True)  # NVARCHAR(120)

    class Meta:
        table_name = 'Artist'

class Album(BaseModel):
    album_id = AutoField(column_name='AlbumId')
    artist = ForeignKeyField(column_name='ArtistId', field='artist_id', model=Artist)
    title = UnknownField(column_name='Title')  # NVARCHAR(160)

    class Meta:
        table_name = 'Album'

class Employee(BaseModel):
    address = UnknownField(column_name='Address', null=True)  # NVARCHAR(70)
    birth_date = DateTimeField(column_name='BirthDate', null=True)
    city = UnknownField(column_name='City', null=True)  # NVARCHAR(40)
    country = UnknownField(column_name='Country', null=True)  # NVARCHAR(40)
    email = UnknownField(column_name='Email', null=True)  # NVARCHAR(60)
    employee_id = AutoField(column_name='EmployeeId')
    fax = UnknownField(column_name='Fax', null=True)  # NVARCHAR(24)
    first_name = UnknownField(column_name='FirstName')  # NVARCHAR(20)
    hire_date = DateTimeField(column_name='HireDate', null=True)
    last_name = UnknownField(column_name='LastName')  # NVARCHAR(20)
    phone = UnknownField(column_name='Phone', null=True)  # NVARCHAR(24)
    postal_code = UnknownField(column_name='PostalCode', null=True)  # NVARCHAR(10)
    reports_to = ForeignKeyField(column_name='ReportsTo', field='employee_id', model='self', null=True)
    state = UnknownField(column_name='State', null=True)  # NVARCHAR(40)
    title = UnknownField(column_name='Title', null=True)  # NVARCHAR(30)

    class Meta:
        table_name = 'Employee'

class Customer(BaseModel):
    address = UnknownField(column_name='Address', null=True)  # NVARCHAR(70)
    city = UnknownField(column_name='City', null=True)  # NVARCHAR(40)
    company = UnknownField(column_name='Company', null=True)  # NVARCHAR(80)
    country = UnknownField(column_name='Country', null=True)  # NVARCHAR(40)
    customer_id = AutoField(column_name='CustomerId')
    email = UnknownField(column_name='Email')  # NVARCHAR(60)
    fax = UnknownField(column_name='Fax', null=True)  # NVARCHAR(24)
    first_name = UnknownField(column_name='FirstName')  # NVARCHAR(40)
    last_name = UnknownField(column_name='LastName')  # NVARCHAR(20)
    phone = UnknownField(column_name='Phone', null=True)  # NVARCHAR(24)
    postal_code = UnknownField(column_name='PostalCode', null=True)  # NVARCHAR(10)
    state = UnknownField(column_name='State', null=True)  # NVARCHAR(40)
    support_rep = ForeignKeyField(column_name='SupportRepId', field='employee_id', model=Employee, null=True)

    class Meta:
        table_name = 'Customer'

class Genre(BaseModel):
    genre_id = AutoField(column_name='GenreId')
    name = UnknownField(column_name='Name', null=True)  # NVARCHAR(120)

    class Meta:
        table_name = 'Genre'

class Invoice(BaseModel):
    billing_address = UnknownField(column_name='BillingAddress', null=True)  # NVARCHAR(70)
    billing_city = UnknownField(column_name='BillingCity', null=True)  # NVARCHAR(40)
    billing_country = UnknownField(column_name='BillingCountry', null=True)  # NVARCHAR(40)
    billing_postal_code = UnknownField(column_name='BillingPostalCode', null=True)  # NVARCHAR(10)
    billing_state = UnknownField(column_name='BillingState', null=True)  # NVARCHAR(40)
    customer = ForeignKeyField(column_name='CustomerId', field='customer_id', model=Customer)
    invoice_date = DateTimeField(column_name='InvoiceDate')
    invoice_id = AutoField(column_name='InvoiceId')
    total = DecimalField(column_name='Total')

    class Meta:
        table_name = 'Invoice'

class MediaType(BaseModel):
    media_type_id = AutoField(column_name='MediaTypeId')
    name = UnknownField(column_name='Name', null=True)  # NVARCHAR(120)

    class Meta:
        table_name = 'MediaType'

class Track(BaseModel):
    album = ForeignKeyField(column_name='AlbumId', field='album_id', model=Album, null=True)
    bytes = IntegerField(column_name='Bytes', null=True)
    composer = UnknownField(column_name='Composer', null=True)  # NVARCHAR(220)
    genre = ForeignKeyField(column_name='GenreId', field='genre_id', model=Genre, null=True)
    media_type = ForeignKeyField(column_name='MediaTypeId', field='media_type_id', model=MediaType)
    milliseconds = IntegerField(column_name='Milliseconds')
    name = UnknownField(column_name='Name')  # NVARCHAR(200)
    track_id = AutoField(column_name='TrackId')
    unit_price = DecimalField(column_name='UnitPrice')

    class Meta:
        table_name = 'Track'

class InvoiceLine(BaseModel):
    invoice = ForeignKeyField(column_name='InvoiceId', field='invoice_id', model=Invoice)
    invoice_line_id = AutoField(column_name='InvoiceLineId')
    quantity = IntegerField(column_name='Quantity')
    track = ForeignKeyField(column_name='TrackId', field='track_id', model=Track)
    unit_price = DecimalField(column_name='UnitPrice')

    class Meta:
        table_name = 'InvoiceLine'

class Playlist(BaseModel):
    name = UnknownField(column_name='Name', null=True)  # NVARCHAR(120)
    playlist_id = AutoField(column_name='PlaylistId')

    class Meta:
        table_name = 'Playlist'

class PlaylistTrack(BaseModel):
    playlist = ForeignKeyField(column_name='PlaylistId', field='playlist_id', model=Playlist)
    track = ForeignKeyField(column_name='TrackId', field='track_id', model=Track)

    class Meta:
        table_name = 'PlaylistTrack'
        indexes = (
            (('playlist', 'track'), True),
            (('playlist', 'track'), True),
        )
        primary_key = CompositeKey('playlist', 'track')

