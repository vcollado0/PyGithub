# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import GistHistoryState
import NamedUser
import Gist
import GistComment

class Gist( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )
        self.__completed = completion != LazyCompletion
        if completion == ImmediateCompletion:
            self.__complete() # pragma: no cover

    @property
    def comments( self ):
        self.__completeIfNeeded( self.__comments )
        return self.__comments

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def description( self ):
        self.__completeIfNeeded( self.__description )
        return self.__description

    @property
    def files( self ):
        self.__completeIfNeeded( self.__files )
        return self.__files

    @property
    def fork_of( self ):
        self.__completeIfNeeded( self.__fork_of )
        return self.__fork_of

    @property
    def forks( self ):
        self.__completeIfNeeded( self.__forks )
        return self.__forks

    @property
    def git_pull_url( self ):
        self.__completeIfNeeded( self.__git_pull_url )
        return self.__git_pull_url

    @property
    def git_push_url( self ):
        self.__completeIfNeeded( self.__git_push_url )
        return self.__git_push_url

    @property
    def history( self ):
        self.__completeIfNeeded( self.__history )
        return self.__history

    @property
    def html_url( self ):
        self.__completeIfNeeded( self.__html_url )
        return self.__html_url

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def public( self ):
        self.__completeIfNeeded( self.__public )
        return self.__public

    @property
    def updated_at( self ):
        self.__completeIfNeeded( self.__updated_at )
        return self.__updated_at

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    @property
    def user( self ):
        self.__completeIfNeeded( self.__user )
        return self.__user

    def create_comment( self, body ):
        post_parameters = {
            "body": body,
        }
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/comments",
            None,
            post_parameters
        )
        return GistComment.GistComment( self.__requester, data, completion = NoCompletion )

    def create_fork( self ):
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/fork",
            None,
            None
        )
        return Gist( self.__requester, data, completion = NoCompletion )

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )

    def edit( self, description = DefaultValueForOptionalParameters, files = DefaultValueForOptionalParameters ):
        post_parameters = {
        }
        if description is not DefaultValueForOptionalParameters:
            post_parameters[ "description" ] = description
        if files is not DefaultValueForOptionalParameters:
            post_parameters[ "files" ] = files
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def get_comment( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/gists/comments/" + str( id ),
            None,
            None
        )
        return GistComment.GistComment( self.__requester, data, completion = NoCompletion )

    def get_comments( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/comments",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            GistComment.GistComment,
            self.__requester,
            headers,
            data
        )

    def is_starred( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/star",
            None,
            None
        )
        return status == 204

    def reset_starred( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ) + "/star",
            None,
            None
        )

    def set_starred( self ):
        status, headers, data = self.__requester.request(
            "PUT",
            str( self.url ) + "/star",
            None,
            None
        )

    def __initAttributes( self ):
        self.__comments = None
        self.__created_at = None
        self.__description = None
        self.__files = None
        self.__fork_of = None
        self.__forks = None
        self.__git_pull_url = None
        self.__git_push_url = None
        self.__history = None
        self.__html_url = None
        self.__id = None
        self.__public = None
        self.__updated_at = None
        self.__url = None
        self.__user = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete() # pragma: no cover

    def __complete( self ): # pragma: no cover
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "comments", "created_at", "description", "files", "fork_of", "forks", "git_pull_url", "git_push_url", "history", "html_url", "id", "public", "updated_at", "url", "user", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "comments" in attributes and attributes[ "comments" ] is not None:
            assert isinstance( attributes[ "comments" ], int )
            self.__comments = attributes[ "comments" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None:
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) )
            self.__created_at = attributes[ "created_at" ]
        if "description" in attributes and attributes[ "description" ] is not None:
            assert isinstance( attributes[ "description" ], ( str, unicode ) )
            self.__description = attributes[ "description" ]
        if "files" in attributes and attributes[ "files" ] is not None:
            self.__files = attributes[ "files" ]
        if "fork_of" in attributes and attributes[ "fork_of" ] is not None:
            assert isinstance( attributes[ "fork_of" ], dict )
            self.__fork_of = Gist( self.__requester, attributes[ "fork_of" ], completion = LazyCompletion )
        if "forks" in attributes and attributes[ "forks" ] is not None:
            assert isinstance( attributes[ "forks" ], list ) and ( len( attributes[ "forks" ] ) == 0 or isinstance( attributes[ "forks" ][ 0 ], dict ) )
            self.__forks = [
                Gist( self.__requester, element, completion = LazyCompletion )
                for element in attributes[ "forks" ]
            ]
        if "git_pull_url" in attributes and attributes[ "git_pull_url" ] is not None:
            assert isinstance( attributes[ "git_pull_url" ], ( str, unicode ) )
            self.__git_pull_url = attributes[ "git_pull_url" ]
        if "git_push_url" in attributes and attributes[ "git_push_url" ] is not None:
            assert isinstance( attributes[ "git_push_url" ], ( str, unicode ) )
            self.__git_push_url = attributes[ "git_push_url" ]
        if "history" in attributes and attributes[ "history" ] is not None:
            assert isinstance( attributes[ "history" ], list ) and ( len( attributes[ "history" ] ) == 0 or isinstance( attributes[ "history" ][ 0 ], dict ) )
            self.__history = [
                GistHistoryState.GistHistoryState( self.__requester, element, completion = LazyCompletion )
                for element in attributes[ "history" ]
            ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None:
            assert isinstance( attributes[ "html_url" ], ( str, unicode ) )
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None:
            assert isinstance( attributes[ "id" ], ( str, unicode ) )
            self.__id = attributes[ "id" ]
        if "public" in attributes and attributes[ "public" ] is not None:
            assert isinstance( attributes[ "public" ], bool )
            self.__public = attributes[ "public" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None:
            assert isinstance( attributes[ "updated_at" ], ( str, unicode ) )
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
        if "user" in attributes and attributes[ "user" ] is not None:
            assert isinstance( attributes[ "user" ], dict )
            self.__user = NamedUser.NamedUser( self.__requester, attributes[ "user" ], completion = LazyCompletion )
