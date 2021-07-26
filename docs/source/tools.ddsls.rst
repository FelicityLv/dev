DDSLS
=====

Introduction
------------

When using DDS, it's sometimes useful to know what DDS entities are running in the system. The `DDSLS <https://github.com/YixianLv/cyclonedds-python/tree/tools/src/cyclonedds/cyclonedds/tools/ddsls>`_ is a tool that subscribes to the Built-in topics, and shows the information of the domain participants, data readers and data writers in the system.


Usage
-----

To run the DDSLS tool, you can use:

.. code-block::

    python3 -m ddsls [Options]

There are several options you can choose to use the DDSLS tool according to your needs, which will be further explained in the following sections.

For checking the DDS entity information, you can use the ``--topic`` or ``--all`` option to specify which entity's information you want to see, the ``--id`` option to define which domain you like to check using the id of the domain participant, the ``--watch`` option to monitor the changes in the system as entities being created and disposed.

For viewing options, you can use the ``--json`` option to view the output data in JSON format, the ``--verbose`` option to view the full sample information when the entity's QoS changes.

For additional options, you can use the ``--filename`` option to define the name of file you want to output the result to, the ``--runtime`` option to specify how long the DDSLS tool will run.

Topic
^^^^^

To use the DDSLS tool, you need to specify the topic you're subscribing to using the ``--topic`` or ``--all`` option.

For ``--topic`` option, you can choose from ``dcpsparticipant``, ``dcpssubscription`` and ``dcpspublication``.

The ``dcpsparticipant``, ``dcpssubscription`` and ``dcpspublication`` subscribes to the **BuiltinTopicDcpsParticipant**, **BuiltinTopicSubscription** and **BuiltinTopicDcpsPublication** topic respectively, and will show the information of all the participants, subscribers and publishers in the domain respectively.

Here's an example of running DDSLS with the ``dcpsparticipant`` topic, run the command:

.. code-block::

    python3 -m ddsls --all

If there are DDS participant, data reader and data writer running in the default domain, it will show up in the DDSLS tool like this:

.. image:: ./figs/ddsls/all.png
    :width: 800


Comprehend output
"""""""""""""""""

* The result above shows that there is two participant, one data reader and one data writer running in the default domain;

* **New** in "New PARTICIPANT", "New SUBSCRIPTION", "New PUBLICATION" indicates that the entities are alive. If the entities are no longer alive, the message will be **Disposed** instead, such as "Disposed PARTICIPANT".

* And the fields for the entities are:

  * **PARTICIPANT**:

    * **key**: The GUID (Globally Unique Identifier) of the domain participant.

  * **SUBSCRIPTION** and **PUBLICATION**:

    * **key**: The GUID of the data reader or data writer;
    * **participant_key**: The GUID of the domain participant that created the data reader or data writer;
    * **participant_instance_handle**: The instance handle of the domain participant;
    * **topic_name**: The name of the topic that the data reader / data writer is subscribing / writing to;
    * **type_name**: The type name used in the topic of the data reader / data writer;
    * **qos**: The QoS (Quality of Service) of the data reader / data writer.

Domain participant id
^^^^^^^^^^^^^^^^^^^^^

By default, the DDSLS tool subscribes to the default domain (domain 0) and displays information of entities in that domain. However, if you want to view the entity information in another domain, you can use the option ``-- id`` to change the domain to which the DDSLS tool subscribes.

The ``--id`` option will set the id of the DDSLS domain participant, allowing the DDSLS tool to view entities in the domain you chooses.

For example, if you run a small script using domain 1 as the domain participant:

.. code-block:: python
    :linenos:

    from cyclonedds.domain import DomainParticipant

    dp = DomainParticipant(1)

If you run ``python3 -m ddsls --topic dcpsparticipant``, the participant you've just created will not be there, since it's only viewing entities in the default domain. To view this participant information, you need to use:

.. code-block::

    python3 -m ddsls --topic dcpsparticipant --id 1

And the result of the participant in domain 1 will be:

.. image:: ./figs/ddsls/id.png
    :width: 400


Watch mode
^^^^^^^^^^
By default, the DDSLS tool will run for 1 second and then automatically exit. However, if you want to monitor the entities in the system, you can use the ``--watch`` option to enable the watch mode.

In watch mode, the DDSLS tool will not automatically exit (if the ``--runtime`` option is not selected).  The watch mode will monitor the entities as they are being created and disposed, and display the entity information.


For example, if you have the DDSLS tool monitoring the ``dcpsparticipant`` topic, using the command:

.. code-block::

    python3 -m ddsls --topic dcpsparticipant --watch

Then start and exit a script that creates a domain participant entity in the default domain.

Verbose mode
^^^^^^^^^^^^


Write to file
^^^^^^^^^^^^^


Runtime
^^^^^^^

