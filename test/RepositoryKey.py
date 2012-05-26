import Framework

class RepositoryKey( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.key = self.g.get_user().get_repo( "PyGithub" ).get_key( 2626761 )

    def testAttributes( self ):
        self.assertEqual( self.key.id, 2626761 )
        self.assertEqual( self.key.key, "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA2Mm0RjTNAYFfSCtUpO54usdseroUSIYg5KX4JoseTpqyiB/hqewjYLAdUq/tNIQzrkoEJWSyZrQt0ma7/YCyMYuNGd3DU6q6ZAyBeY3E9RyCiKjO3aTL2VKQGFvBVVmGdxGVSCITRphAcsKc/PF35/fg9XP9S0anMXcEFtdfMHz41SSw+XtE+Vc+6cX9FuI5qUfLGbkv8L1v3g4uw9VXlzq4GfTA+1S7D6mcoGHopAIXFlVr+2RfDKdSURMcB22z41fljO1MW4+zUS/4FyUTpL991es5fcwKXYoiE+x06VJeJJ1Krwx+DZj45uweV6cHXt2JwJEI9fWB6WyBlDejWw==" )
        self.assertEqual( self.key.title, "Key added through PyGithub" )
        self.assertEqual( self.key.url, "https://api.github.com/user/keys/2626761" )
        self.assertEqual( self.key.verified, True )

    def testEdit( self ):
        pass
        ### @todo Custom URL
        # self.key.edit( "Title edited by PyGithub", "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA5Q58YmzZjU64prR5Pk91MfeHezOTgLqDYmepYbv3qjguiHtPai1vSai5WvUv3hgf9DArXsXE5CV6yoBIhAdGtpJKExHuQ2m4XTFCdbrgfQ3ypcSdgzEiQemyTA6TWwhbuwjJ1IqJMYOVLH+FBCkD8pyIpUDO7v3vaR2TCEuNwOS7lbsRsW3OkGYnUKjaPaCTe/inrqb7I3OE8cPhWJ3dM/zzzBj22J4LCNKhjKua8TFS74xGm3lNDZ6/twQl4n4xmrH/3tG+WOJicNO3JohNHqK9T0pILnr3epEyfdkBjcG0qXApqWvH2WipJhaH6of8Gdr0Z/K/7p8QFddmwNgdPQ==" )
        # self.assertEqual( self.key.key, "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA5Q58YmzZjU64prR5Pk91MfeHezOTgLqDYmepYbv3qjguiHtPai1vSai5WvUv3hgf9DArXsXE5CV6yoBIhAdGtpJKExHuQ2m4XTFCdbrgfQ3ypcSdgzEiQemyTA6TWwhbuwjJ1IqJMYOVLH+FBCkD8pyIpUDO7v3vaR2TCEuNwOS7lbsRsW3OkGYnUKjaPaCTe/inrqb7I3OE8cPhWJ3dM/zzzBj22J4LCNKhjKua8TFS74xGm3lNDZ6/twQl4n4xmrH/3tG+WOJicNO3JohNHqK9T0pILnr3epEyfdkBjcG0qXApqWvH2WipJhaH6of8Gdr0Z/K/7p8QFddmwNgdPQ==" )
        # self.assertEqual( self.key.title, "Title edited by PyGithub" )

    def testDelete( self ):
        pass
        ### @todo Custom URL
        # self.key.delete()
