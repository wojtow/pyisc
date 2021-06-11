# Copyright 2021 Jonas Hallqvist

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Manipulates ISC named configuration files.

Enables the conversion of ISC named conf file to a tree like structure
of objects suitable for alteration and the conversation of that
structure to a string that can easily be written to a file and read by
named daemon.

Example:
    Load file and add statement:

        >>> from pyisc import bind
        >>> with open('etc/named.conf', 'r') as infile:
        ...     isc_config = infile.read()
        >>> isc_tree = bind.loads(isc_config)
        >>> print(bind.dumps(isc_tree))
        options {
            directory "/var/lib/named";
            dump-file "/var/log/named_dump.db";
            statistics-file "/var/log/named.stats";
        # The forwarders record contains a list of servers to which
        # queries should be forwarded.  Up to three servers may be
        # listed.
            forwarders {
                62.31.176.39;
                193.38.113.3;
            };
        # Enable the next entry to prefer usage of the name server
        # declared in the forwarders section.
        #forward first;
            listen-on-v6 {
                any;
            };
        # If notify is set to yes (default), notify messages are sent
        # to other name servers when the zone data is changed. Instead
        # of setting a global 'notify' statement in the 'options'
        # section, a separate 'notify' can be added to each zone
        # definition.
            notify no;
        };
        # The following zone definitions don't need any modification.
        # The first one is the definition of the root name servers.
        # The second one defines localhost while the third defines the
        # reverse lookup for localhost.
        zone "." in {
            type hint;
            file "root.hint";
        };
        zone "localhost" in {
            type master;
            file "localhost.zone";
        };
        zone "0.0.127.in-addr.arpa" in {
            type master;
            file "127.0.0.zone";
        };
        # This is where you put in the link to the zone you
        # want to serve
        zone "spring.wellho.net" in {
            type master;
            file "/var/lib/named/wellho.zone";
        };
        # Include the meta include file generated by create
        # NamedConfInclude. This includes all files as configured in
        # NAMED_CONF_INCLUDE_FILES from /etc/sysconfig/named
        include "/etc/named.conf.include";
        >>> new_node = shared.nodes.PropertyNode(
        ...    type='allow-new-zones',
        ...    value='yes',
        ...    parameters=None)
        >>> isc_tree.children[0].children.append(new_node)
        >>> print(bind.dumps(isc_tree))
        options {
            allow-new-zones yes;
            directory "/var/lib/named";
            dump-file "/var/log/named_dump.db";
            statistics-file "/var/log/named.stats";
        # The forwarders record contains a list of servers to which
        # queries should be forwarded.  Up to three servers may be
        # listed.
            forwarders {
                62.31.176.39;
                193.38.113.3;
            };
        # Enable the next entry to prefer usage of the name server
        # declared in the forwarders section.
        #forward first;
            listen-on-v6 {
                any;
            };
        # If notify is set to yes (default), notify messages are sent
        # to other name servers when the zone data is changed. Instead
        # of setting a global 'notify' statement in the 'options'
        # section, a separate 'notify' can be added to each zone
        # definition.
            notify no;
        };
        # The following zone definitions don't need any modification.
        # The first one is the definition of the root name servers.
        # The second one defines localhost while the third defines the
        # reverse lookup for localhost.
        zone "." in {
            type hint;
            file "root.hint";
        };
        zone "localhost" in {
            type master;
            file "localhost.zone";
        };
        zone "0.0.127.in-addr.arpa" in {
            type master;
            file "127.0.0.zone";
        };
        # This is where you put in the link to the zone you
        # want to serve
        zone "spring.wellho.net" in {
            type master;
            file "/var/lib/named/wellho.zone";
        };
        # Include the meta include file generated by create
        # NamedConfInclude. This includes all files as configured in
        # NAMED_CONF_INCLUDE_FILES from /etc/sysconfig/named
        include "/etc/named.conf.include";

Attributes:
    dumps (object): Returns a string created from a PyISC Named object
        tree.
    loads (string): Returns a PyISC Named object tree from a supplied
        string.

"""

__all__ = ['dumps', 'loads', 'print_tree', 'sort_tree']
__version__ = '0.2.0'
__author__ = 'Jonas Hallqvist'

# from pyisc.shared.nodes import Node, PropertyNode
# from pyisc.shared.utils import sort_tree_algorithm
from pyisc.shared.utils import print_tree, sort_tree, string_constructor
from pyisc.bind.parsing import BindParser


def loads(content):
    """Return a PyISC object tree from a supplied string.

    Takes a string, either a custom one or one read from a file, and
    converts it to a PyISC object tree.

    Args:
        content (str): The string that should be converted.

    Returns:
        pyisc.shared.nodes.RootNode: A tree like representation of the
            supplied string.

    Examples:
        >>> from pyisc import bind
        >>> with open('tests/named.conf', 'r') as infile:
        ...     isc_config = infile.read()
        >>> isc_tree = bind.loads(isc_config)
        >>> isc_tree
        RootNode(Root)

    """
    parser = BindParser()
    return parser.build_tree(content)


def dumps(tree, enable_comments=True):
    r"""Return a string of the PyISC object tree.

    This function takes a PyISC object tree structure and converts it
    to a string ready to be written to a file.

    Args:
        tree (pyisc.shared.nodes.RootNode): The tree structure.
        enable_comments (boolean): Determines if the function will include
            comments or not in the generated string.

    Returns:
        str: A complete string that is ready to write to a suitable
            file.

    Examples:
        >>> from pyisc import bind
        >>> bind.dumps(isc_tree)
        'zone "example.com" {\n    type master;\n};\n'

    """
    section_end = '};'
    result = ''
    level = 0
    return string_constructor(**locals())
