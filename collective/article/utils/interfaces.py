#!/usr/bin/python
# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import Interface
from collective.article import MessageFactory as _
from ..utils.vocabularies import _createPriorityVocabulary, _createInsuranceTypeVocabulary
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

priority_vocabulary = SimpleVocabulary(list(_createPriorityVocabulary()))
insurance_type_vocabulary = SimpleVocabulary(list(_createInsuranceTypeVocabulary()))

class ListField(schema.List):
    """We need to have a unique class for the field list so that we
    can apply a custom adapter."""
    pass

# # # # # # # # # # # # #
# Widget interface      #
# # # # # # # # # # # # #

class IFormWidget(Interface):
    pass


# # # # # # # # # # # # # #
# DataGrid interfaces     # 
# # # # # # # # # # # # # #

# Title and author
class ITitle(Interface):
    title = schema.TextLine(title=_(u'Title'), required=False)

    
class IAuthor(Interface):
    author = schema.TextLine(title=_(u'Author'), required=False)
    role = schema.TextLine(title=_(u'Role'), required=False)

class IIllustrator(Interface):
    illustrator = schema.TextLine(title=_(u'Illustrator'), required=False)
    role = schema.TextLine(title=_(u'Role'), required=False)

class IPlace(Interface):
    term =  schema.TextLine(title=_(u'Place'), required=False)

class IPublisher(Interface):
    term = schema.TextLine(title=_(u'Publisher'), required=False)

class IPlacePrinted(Interface):
    term = schema.TextLine(title=_(u'Place printed'), required=False)

class IPrinter(Interface):
    name = schema.TextLine(title=_(u'Printer'), required=False)

class IAccompanyingMaterial(Interface):
    term = schema.TextLine(title=_(u'Accompanying material'), required=False)

class IPhysicalDetails(Interface):
    term = schema.TextLine(title=_(u'Physical detail'), required=False)

class IBibliographicalNotes(Interface):
    term = schema.TextLine(title=_(u'Bibliographical notes'), required=False)

class IConference(Interface):
    term = schema.TextLine(title=_(u'Conference'), required=False)

class ISource(Interface):
    sourceTitleArticle = schema.TextLine(title=_(u'Source title article'), required=False)
    materialType = schema.TextLine(title=_(u'Material type'), required=False)
    sourceTitle = schema.TextLine(title=_(u'Source title'), required=False)
    volume = schema.TextLine(title=_(u'Volume'), required=False)
    issue = schema.TextLine(title=_(u'Issue'), required=False)
    day = schema.TextLine(title=_(u'Day'), required=False)
    month = schema.TextLine(title=_(u'Month'), required=False)
    year = schema.TextLine(title=_(u'Year'), required=False)
    pagination = schema.TextLine(title=_(u'Pagination'), required=False)
    notes = schema.TextLine(title=_(u'Notes'), required=False)

class IIllustrations(Interface):
    term = schema.TextLine(title=_(u'Illustrations'), required=False)


# Abstract and subject terms
class IMaterialType(Interface):
    term = schema.TextLine(title=_(u'Material type'), required=False)

class IBiblForm(Interface):
    term = schema.TextLine(title=_(u'Bibl. form'), required=False)

class ILanguage(Interface):
    term = schema.TextLine(title=_(u'Language'), required=False)

class INotes(Interface):
    note = schema.TextLine(title=_(u'Notes'), required=False)


class IClassNumber(Interface):
    term = schema.TextLine(title=_(u'Class number'), required=False)

class ISubjectTerm(Interface):
    subjectTermType = schema.TextLine(title=_(u'Subject term type'), required=False)
    subjectType = schema.TextLine(title=_(u'Subject term'), required=False)
    properName = schema.TextLine(title=_(u'Proper name'), required=False)

class IPersonKeywordType(Interface):
    personKeywordType = schema.TextLine(title=_(u'Person keyword type'), required=False)
    name = schema.TextLine(title=_(u'Name'), required=False)
    role = schema.TextLine(title=_(u'Role'), required=False)

class IGeographicalKeyword(Interface):
    term = schema.TextLine(title=_(u'Geographical keyword'), required=False)

class IPeriod(Interface):
    term = schema.TextLine(title=_(u'Period'), required=False)

class IDigitalReferences(Interface):
    reference = schema.TextLine(title=_(u'Reference'), required=False)

class IAbstract(Interface):
    term = schema.TextLine(title=_(u'Abstract'), required=False)

# Reproductions
class IReproduction(Interface):
    reference = schema.TextLine(title=_(u'Reference'), required=False)
    type = schema.TextLine(title=_(u'Type'), required=False)
    format = schema.TextLine(title=_(u'Format'), required=False)
    date = schema.TextLine(title=_(u'Date'), required=False)
    identifierURL = schema.TextLine(title=_(u'Identifier (URL)'), required=False)
    notes = schema.TextLine(title=_(u'Notes'), required=False)


# Exhibitions, auctions, collections
class IExhibition(Interface):
    exhibitionName = schema.TextLine(title=_(u'Exhibition name'), required=False)
    date = schema.TextLine(title=_(u'Date'), required=False)
    to = schema.TextLine(title=_(u'to'), required=False)
    organiser = schema.TextLine(title=_(u'Organiser'), required=False)
    venue = schema.TextLine(title=_(u'Venue'), required=False)
    place = schema.TextLine(title=_(u'Place'), required=False)
    notes = schema.TextLine(title=_(u'Notes'), required=False)


class IAuction(Interface):
    auctionName = schema.TextLine(title=_(u'Auction name'), required=False)
    auctioneer = schema.TextLine(title=_(u'Auctioneer'), required=False)
    date = schema.TextLine(title=_(u'Date'), required=False)
    to = schema.TextLine(title=_(u'to'), required=False)
    place = schema.TextLine(title=_(u'Place'), required=False)
    location = schema.TextLine(title=_(u'Location'), required=False)
    collector = schema.TextLine(title=_(u'Collector'), required=False)
    commissairPriseur = schema.TextLine(title=_(u'Commissair-priseur'), required=False)
    auctionNumber = schema.TextLine(title=_(u'Auction number'), required=False)
    notes = schema.TextLine(title=_(u'Notes'), required=False)

class ICollection(Interface):
    collectionName = schema.TextLine(title=_(u'Collection name'), required=False)
    collector = schema.TextLine(title=_(u'Collector'), required=False)
    organisation = schema.TextLine(title=_(u'Organisation'), required=False)
    date = schema.TextLine(title=_(u'Date'), required=False)
    place = schema.TextLine(title=_(u'Place'), required=False)
    notes = schema.TextLine(title=_(u'Notes'), required=False)


# Relations
class IPartOf(Interface):
    term = schema.TextLine(title=_(u'Part of'), required=False)

class IConsistsOf(Interface):
    term = schema.TextLine(title=_(u'Consists of'), required=False)

class IMuseumObjects(Interface):
    objectNo = schema.TextLine(title=_(u'Object no.'), required=False)
    objectName = schema.TextLine(title=_(u'Object name'), required=False)
    title = schema.TextLine(title=_(u'Title'), required=False)
    maker = schema.TextLine(title=_(u'Maker'), required=False)

# Free fields
class IFreeFields(Interface):
    date = schema.TextLine(title=_(u'Date'), required=False)
    type = schema.TextLine(title=_(u'Type'), required=False)
    confidential = schema.TextLine(title=_(u'Confidential'), required=False)
    contents = schema.TextLine(title=_(u'Contents'), required=False)


class IOtherNumber(Interface):
    type = schema.TextLine(title=_(u'Type'), required=False)
    contents = schema.TextLine(title=_(u'Contents'), required=False)


class ICopyDetails(Interface):
    copyNumber = schema.TextLine(title=_(u'Copy number'), required=False)
    shelfMark = schema.TextLine(title=_(u'Shelf mark'), required=False)
    availability = schema.TextLine(title=_(u'Availability'), required=False)
    loanCategory = schema.TextLine(title=_(u'Loan category'), required=False)
    site = schema.TextLine(title=_(u'Site'), required=False)
    locationNotes = schema.TextLine(title=_(u'Location notes'), required=False)

