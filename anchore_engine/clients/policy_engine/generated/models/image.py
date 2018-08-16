# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Image(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'digest': 'str',
        'user_id': 'str',
        'state': 'str',
        'distro_namespace': 'str',
        'created_at': 'datetime',
        'last_modified': 'datetime',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'digest': 'digest',
        'user_id': 'user_id',
        'state': 'state',
        'distro_namespace': 'distro_namespace',
        'created_at': 'created_at',
        'last_modified': 'last_modified',
        'tags': 'tags'
    }

    def __init__(self, id=None, digest=None, user_id=None, state=None, distro_namespace=None, created_at=None, last_modified=None, tags=None):  # noqa: E501
        """Image - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._digest = None
        self._user_id = None
        self._state = None
        self._distro_namespace = None
        self._created_at = None
        self._last_modified = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if digest is not None:
            self.digest = digest
        if user_id is not None:
            self.user_id = user_id
        if state is not None:
            self.state = state
        if distro_namespace is not None:
            self.distro_namespace = distro_namespace
        if created_at is not None:
            self.created_at = created_at
        if last_modified is not None:
            self.last_modified = last_modified
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this Image.  # noqa: E501


        :return: The id of this Image.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Image.


        :param id: The id of this Image.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def digest(self):
        """Gets the digest of this Image.  # noqa: E501


        :return: The digest of this Image.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this Image.


        :param digest: The digest of this Image.  # noqa: E501
        :type: str
        """

        self._digest = digest

    @property
    def user_id(self):
        """Gets the user_id of this Image.  # noqa: E501


        :return: The user_id of this Image.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Image.


        :param user_id: The user_id of this Image.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def state(self):
        """Gets the state of this Image.  # noqa: E501

        State of the image in the policy evaluation system  # noqa: E501

        :return: The state of this Image.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Image.

        State of the image in the policy evaluation system  # noqa: E501

        :param state: The state of this Image.  # noqa: E501
        :type: str
        """
        allowed_values = ["failed", "initializing", "analyzing", "analyzed"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def distro_namespace(self):
        """Gets the distro_namespace of this Image.  # noqa: E501

        The namespace identifier for this image for purposes of CVE matches, etc  # noqa: E501

        :return: The distro_namespace of this Image.  # noqa: E501
        :rtype: str
        """
        return self._distro_namespace

    @distro_namespace.setter
    def distro_namespace(self, distro_namespace):
        """Sets the distro_namespace of this Image.

        The namespace identifier for this image for purposes of CVE matches, etc  # noqa: E501

        :param distro_namespace: The distro_namespace of this Image.  # noqa: E501
        :type: str
        """

        self._distro_namespace = distro_namespace

    @property
    def created_at(self):
        """Gets the created_at of this Image.  # noqa: E501

        The timestamp on when this image record was created, not the image itself  # noqa: E501

        :return: The created_at of this Image.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Image.

        The timestamp on when this image record was created, not the image itself  # noqa: E501

        :param created_at: The created_at of this Image.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def last_modified(self):
        """Gets the last_modified of this Image.  # noqa: E501

        Time the image record in this service was last updated  # noqa: E501

        :return: The last_modified of this Image.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this Image.

        Time the image record in this service was last updated  # noqa: E501

        :param last_modified: The last_modified of this Image.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def tags(self):
        """Gets the tags of this Image.  # noqa: E501

        List of tags currently applied to the image. Updated by new tag events. Similarly scoped by the user_id  # noqa: E501

        :return: The tags of this Image.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Image.

        List of tags currently applied to the image. Updated by new tag events. Similarly scoped by the user_id  # noqa: E501

        :param tags: The tags of this Image.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list([x.to_dict() if hasattr(x, "to_dict") else x for x in value])
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict([(item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item for item in list(value.items())])
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
