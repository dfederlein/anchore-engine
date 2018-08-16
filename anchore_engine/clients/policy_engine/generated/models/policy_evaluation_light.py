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

from anchore_engine.clients.policy_engine.generated.models.policy import Policy  # noqa: F401,E501
from anchore_engine.clients.policy_engine.generated.models.policy_evaluation_problem import PolicyEvaluationProblem  # noqa: F401,E501
from anchore_engine.clients.policy_engine.generated.models.whitelist import Whitelist  # noqa: F401,E501


class PolicyEvaluationLight(object):
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
        'timestamp': 'str',
        'image_id': 'str',
        'policy': 'Policy',
        'whitelists': 'list[Whitelist]',
        'evaluation_result': 'object',
        'evaluation_problems': 'list[PolicyEvaluationProblem]'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'image_id': 'image_id',
        'policy': 'policy',
        'whitelists': 'whitelists',
        'evaluation_result': 'evaluation_result',
        'evaluation_problems': 'evaluation_problems'
    }

    def __init__(self, timestamp=None, image_id=None, policy=None, whitelists=None, evaluation_result=None, evaluation_problems=None):  # noqa: E501
        """PolicyEvaluationLight - a model defined in Swagger"""  # noqa: E501

        self._timestamp = None
        self._image_id = None
        self._policy = None
        self._whitelists = None
        self._evaluation_result = None
        self._evaluation_problems = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if image_id is not None:
            self.image_id = image_id
        if policy is not None:
            self.policy = policy
        if whitelists is not None:
            self.whitelists = whitelists
        if evaluation_result is not None:
            self.evaluation_result = evaluation_result
        if evaluation_problems is not None:
            self.evaluation_problems = evaluation_problems

    @property
    def timestamp(self):
        """Gets the timestamp of this PolicyEvaluationLight.  # noqa: E501


        :return: The timestamp of this PolicyEvaluationLight.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PolicyEvaluationLight.


        :param timestamp: The timestamp of this PolicyEvaluationLight.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def image_id(self):
        """Gets the image_id of this PolicyEvaluationLight.  # noqa: E501


        :return: The image_id of this PolicyEvaluationLight.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this PolicyEvaluationLight.


        :param image_id: The image_id of this PolicyEvaluationLight.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def policy(self):
        """Gets the policy of this PolicyEvaluationLight.  # noqa: E501


        :return: The policy of this PolicyEvaluationLight.  # noqa: E501
        :rtype: Policy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PolicyEvaluationLight.


        :param policy: The policy of this PolicyEvaluationLight.  # noqa: E501
        :type: Policy
        """

        self._policy = policy

    @property
    def whitelists(self):
        """Gets the whitelists of this PolicyEvaluationLight.  # noqa: E501


        :return: The whitelists of this PolicyEvaluationLight.  # noqa: E501
        :rtype: list[Whitelist]
        """
        return self._whitelists

    @whitelists.setter
    def whitelists(self, whitelists):
        """Sets the whitelists of this PolicyEvaluationLight.


        :param whitelists: The whitelists of this PolicyEvaluationLight.  # noqa: E501
        :type: list[Whitelist]
        """

        self._whitelists = whitelists

    @property
    def evaluation_result(self):
        """Gets the evaluation_result of this PolicyEvaluationLight.  # noqa: E501


        :return: The evaluation_result of this PolicyEvaluationLight.  # noqa: E501
        :rtype: object
        """
        return self._evaluation_result

    @evaluation_result.setter
    def evaluation_result(self, evaluation_result):
        """Sets the evaluation_result of this PolicyEvaluationLight.


        :param evaluation_result: The evaluation_result of this PolicyEvaluationLight.  # noqa: E501
        :type: object
        """

        self._evaluation_result = evaluation_result

    @property
    def evaluation_problems(self):
        """Gets the evaluation_problems of this PolicyEvaluationLight.  # noqa: E501

        list of error objects indicating errors encountered during evaluation execution  # noqa: E501

        :return: The evaluation_problems of this PolicyEvaluationLight.  # noqa: E501
        :rtype: list[PolicyEvaluationProblem]
        """
        return self._evaluation_problems

    @evaluation_problems.setter
    def evaluation_problems(self, evaluation_problems):
        """Sets the evaluation_problems of this PolicyEvaluationLight.

        list of error objects indicating errors encountered during evaluation execution  # noqa: E501

        :param evaluation_problems: The evaluation_problems of this PolicyEvaluationLight.  # noqa: E501
        :type: list[PolicyEvaluationProblem]
        """

        self._evaluation_problems = evaluation_problems

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
        if not isinstance(other, PolicyEvaluationLight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
