Sphinx-pyreverse
=================

**Note: This is not what you will get by doing pip install sphinx-pyreverse.** This has been forked. And for now there
are no plans of merging back.

**No tests are run on this code. I modified decently large amounts to suit my need for one project and do not care
about other uses. If you find a bug or have a question, feel free to ask! If there seems to be interest in this package
I might write some proper doc and tests**

A simple sphinx extension to generate a UML diagram from python modules.

Install
--------

Install should work with: ::

    pip install https://github.com/patou01/sphinx-pyreverse


Usage
------

Add "sphinx_pyreverse" to the extensions list in your conf.py (make sure it is
in the PYTHONPATH).

Call the directive with path to python module as content. ::

    .. uml:: my_module
        :classes: MyClass

Requires pyreverse from pylint.

Arguments
^^^^^^^^^

It should support the standard arguments from pyreverse, but I honestly haven't tested. For instance you can do: ::

    .. uml:: my_module
        :classes: MyClass
        :all-ancestors:

And that should run and give you what you're after...

**Note: depending on your basic config, it will not override nor detect conflict situations. For instance if you put
``all-ancestors`` in the default and then add ``show-ancestors`` in the call to uml, you will get a command containing both**

Options
^^^^^^^

You can write default config to `conf.py`, if an override is found in the arguments, that one will have precedence.

* ``sphinx_pyreverse_output`` (see --output), default is "png"
* ``sphinx_pyreverse_filter_mode`` (see --filter_mode), default is None
* ``sphinx_pyreverse_show_ancestors`` (see --show_ancestors), default is None
* ``sphinx_pyreverse_all_ancestors`` (see --all_ancestors), default is None
* ``sphinx_pyreverse_show_associated`` (see --show_associated), default is None
* ``sphinx_pyreverse_all_associated`` (see --all_associated), default is None
* ``sphinx_pyreverse_show_builtin`` (see --show_builtin), default is None
* ``sphinx_pyreverse_module_names`` (see --module_names), default is None
* ``sphinx_pyreverse_only_classnames`` (see --only_classnames), default is None
* ``sphinx_pyreverse_ignore`` (see --ignore), default is None

Changing the directive
^^^^^^^^^^^^^^^^^^^^^^

To override the directive, which defaults to 'uml' set the
``SPHINX_PYREVERSE_DIRECTIVE`` environment variable to whatever you like.

Troubleshooting
^^^^^^^^^^^^^^^

``sphinx-pyreverse`` uses sphinx-docs' logging api to write information to the log-files.

To use it run your ``sphinx-build`` command with ``-v -v -v -w $(pwd)/sphinx.log`` .

For more information see:

  * `-v switch`_
  * `-w switch`_


.. _-v switch: https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-v
.. _-w switch: https://www.sphinx-doc.org/en/master/man/sphinx-build.html#cmdoption-sphinx-build-w
