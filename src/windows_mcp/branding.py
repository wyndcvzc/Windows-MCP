"""User-visible product identity for this distribution.

This build is a redistribution of an upstream MIT-licensed project. MIT lets a
downstream vendor rename and sell the result, but three constraints shape what
is changed here:

* The upstream copyright notice and permission notice must stay in the tree
  (see ``LICENSE.md`` and ``FORK.md``). Removing them is what turns a lawful
  resale into a copyright claim.
* The vendor must not imply the upstream authors endorse this build. Nothing
  here may present the product as official, and the upstream name must not be
  used as a product name.
* ``Windows`` is a Microsoft trademark. Microsoft's trademark guidelines forbid
  using it as (or as part of) a product name in a way that suggests affiliation,
  so the shipped name is brand-neutral.

Only the identity is swapped. The internal package name ``windows_mcp``, the
``~/.windows-mcp`` config directory and the thread names all stay untouched —
renaming those would break existing installs and diverge from upstream far more
than a rebrand needs to.
"""

from __future__ import annotations

#: Name shown in MCP host UIs, window titles and CLI output.
PRODUCT_NAME = "DeskBuddy"

#: Chinese display name, for the localized build.
PRODUCT_NAME_CN = "桌面搭子"

#: Identifier handed to FastMCP; keep it slug-shaped.
MCP_SERVER_NAME = "deskbuddy"

UPSTREAM_NAME = "Windows-MCP"
UPSTREAM_URL = "https://github.com/CursorTouch/Windows-MCP"
UPSTREAM_COPYRIGHT = "Copyright (c) 2025 JEOMON GEORGE"
UPSTREAM_LICENSE = "MIT"

#: One-line attribution for ``--help`` footers and about boxes. The licence
#: requires the notice to travel with the software; this is the short form that
#: points at the full text.
ATTRIBUTION = f"Based on {UPSTREAM_NAME} ({UPSTREAM_LICENSE}) {UPSTREAM_COPYRIGHT} — {UPSTREAM_URL}"
