.. raw:: latex

   \pagestyle{plain}
   \thispagestyle{plain}

.. _wg-charter:

FG-TIDA WG1: Continuous and Dynamic Remote Attestation for Agentic AI (CDRA)
============================================================================

*Working title, open for revision.*

TL;DR WG1 enables dynamic remote attestation for AI agents that change while they run, and continuous enforcement of the flow of Attestation Results about them.

Charter Information
-------------------

.. list-table::
   :header-rows: 0
   :widths: 30 70

   * - **Charter version**
     - 0.4

   * - **Date**
     - 2026-10-29

   * - **Status**
     - Draft, initial proposal for discussion

1. Group Information
--------------------

..
   MANDATORY

   AUTHOR GUIDANCE:

   Include names and affiliations only in this section.

   Provide the exact repository and issue-tracker link.

   Do not include biographies, honorary titles, or persons who have not
   agreed to serve.

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Field
     - Content

   * - Working group name and acronym
     - Continuous and Dynamic Remote Attestation for Agentic AI (CDRA), working title, presented as Remote Attestation for Agentic AI (RA-AAI)

   * - Basis
     - RA-AAI roadmap v1.0, presented at the FG-TIDA preparation meeting of 30 September 2026

   * - FG-TIDA ToR items covered
     - Clauses 4.2 to 4.5, with Annex A examples A.2.1, A.2.2, A.2.7 and A.2.8

   * - Chair(s) / co-chairs
     - TBD

   * - Editor(s) of the main deliverables
     - TBD

   * - Theme proposers
     - Henk Birkholz, Houda Labiod (Huawei)

   * - Mailing list
     - TBD

   * - Repository and issue tracker
     - https://github.com/fg-tida-wg1/wg1-cdra-charter

   * - Working methods
     - Rough consensus, co-chairs, empowered editors, bi-weekly calls, and workshops or webinars where useful

   * - Charter status and version
     - Draft 0.4

2. Background and Problem Statement
-----------------------------------

..
   MANDATORY

   AUTHOR GUIDANCE:

   Write two to four short paragraphs, or a concise numbered list.

   State:

   - what the problem is;
   - who has the problem: people, organizations, AI agents, systems, etc.;
   - why existing work does not adequately solve it;
   - any essential terms needed to understand the rest of the charter.

   Define only essential terms here.

   Do not include:

   - a history of the topic;
   - a literature review;
   - a proposed solution;
   - claims about a particular vendor or product;
   - undefined buzzwords.

AI agents plan, call tools and act on behalf of people.
Before a service hands an agent a payment, a secret or a production system, it needs to know what is actually running, presented continuously as fresh Evidence.

Remote attestation answers this question in the form of snapshots for platforms today.
An Attester produces Evidence about its state, and a Verifier appraises that Evidence and issues Attestation Results that other services rely on.
This works well for systems that are checked once at start and then stay (mostly) the same.
Evidence from such snapshots demonstrates what code is running where, but not what an agent's context or intent actually is.

Agentic AI breaks these assumptions along three questions.

* What to measure: agents are dynamic composites of model, code, tools, policies and a context of instructions, data and memory, and any part can change at runtime.

* How to appraise and act: each service enforces its own rules on Attestation Results, and agents rely on other agents when they delegate.
  Many legacy services can neither produce Evidence nor read Attestation Results.

* When to refresh: a check at an agent's start-up is not enough to demonstrate the trustworthiness of its next action.
  Therefore, Evidence and Attestation Results about a set of related agents have to flow continuously.

3. Goals
--------

..
   MANDATORY

   AUTHOR GUIDANCE:

   State what the Working Group will produce and why.

   Keep this section to approximately three to six sentences or bullets.

   Make clear whether the WG will:

   - describe: use cases, terminology, gap analysis;
   - specify: formats, interfaces, protocols;
   - recommend: guidelines, principles or best practices.

   The WG should build on relevant existing standards and specifications
   where possible.

   Do not use open-ended language such as "and any other related topics".

   Do not claim authority reserved for ITU-T Study Groups, such as approving
   ITU-T Recommendations.

The Working Group focuses on pre-standardization work toward open, interoperable and privacy-preserving remote attestation of AI agents, so that any user or service can rely on any agent from any environment.

The Working Group describes what to measure, how to appraise and act, and when to refresh, and maps existing building blocks and remaining gaps (Deliverable 1).

* What: The Working Group specifies requirements for Evidence about an agent's dynamically changing parts and a signed manifest of them (Deliverable 2).

* How: The Working Group specifies requirements for enforcing decisions based on Attestation Results, by policy or by technology, even when results are stale, missing or negative (Deliverable 3).
  It also specifies requirements for including legacy systems (Deliverable 4).

* When: The Working Group specifies requirements for keeping Evidence and Attestation Results continuously fresh, with triggers keyed to risk (Deliverable 2).

The Working Group reuses existing specifications where possible and drafts requirements as base material for SG17.

4. Scope and Non-Goals
----------------------

In Scope
~~~~~~~~

..
   MANDATORY

   AUTHOR GUIDANCE:

   Identify clearly what work belongs to this Working Group.

* What: Evidence about an agent's parts, context and observed behaviour, and a signed manifest of its parts, as they change at runtime.

* How: Binding Evidence to the agent's platform and identity, and disclosing it in a privacy-preserving way.

* How: Acting on Attestation Results, including stale or missing ones, and trustworthy enforcement points for the resulting decisions.

* How: Patterns that let legacy systems benefit from remote attestation, such as credentials issued only after a successful appraisal and valid no longer than the appraisal.

* How: If FG-TIDA management confirms this item, requirements for agent interaction protocols to find and carry Evidence and Attestation Results.

* When: Risk-keyed triggers for fresh Evidence and new appraisals, such as elapsed time, restarts, tool calls, delegation and changes to an agent's parts, and how long Attestation Results about a set of related agents stay valid.

Out of Scope / Non-Goals
~~~~~~~~~~~~~~~~~~~~~~~~

..
   MANDATORY

   AUTHOR GUIDANCE:

   Explicitly identify what the WG will NOT do.

   This section is important for preventing scope creep.

   Where a neighbouring topic belongs to another FG-TIDA WG, an SG17
   Question, or another organization, identify that relationship.

   Avoid defining the same deliverable under more than one WG.

The Working Group does not address AI governance or design agent interaction protocols.

The Working Group does not decide on individual agent actions, authorization or privileges, but states requirements on the Attestation Results such decisions rely on.

The Working Group does not define new formats, protocols or languages for Evidence, Attestation Results or appraisal policies, nor agent identifiers or new hardware.

The Working Group does not define training provenance, which it consumes, nor benchmark or evaluate the security of agents.

5. Programme of Work and Deliverables
-------------------------------------

..
   MANDATORY

   AUTHOR GUIDANCE:

   Identify concrete documents the WG intends to produce.

   Every deliverable should have:

   - a clear title;
   - a short description;
   - relevant input documents, where applicable.

   Existing contributions or draft documents should be identified as inputs,
   not automatically treated as adopted WG text.

   Avoid open-ended deliverables such as "ongoing analysis".

.. list-table::
   :header-rows: 1
   :widths: 6 29 45 20

   * - #
     - Deliverable
     - Short description
     - Input documents

   * - 1
     - White paper: Remote Attestation Challenges for Agentic AI Systems (Technical Report)
     - What to measure in an agent, how to appraise Evidence and act on Attestation Results, and when to refresh them, with threats, state of the art, gaps and existing building blocks.
     - WG1 white paper outline (September 2026), RA-AAI roadmap v1.0

   * - 2
     - Requirements for continuous and dynamic remote attestation of agentic AI systems (Technical Specification)
     - What Evidence and a signed agent manifest must demonstrate as an agent's parts change, when fresh Evidence and new appraisals are due, how long Attestation Results about a set of related agents stay valid, and, if confirmed, how agent interactions carry them.
     - Deliverable 1, RA-AAI roadmap v1.0

   * - 3
     - Requirements for acting on Attestation Results (Technical Specification)
     - How services and agents that rely on Attestation Results behave by default, handle stale, missing or negative results, record the Attestation Results a decision used, and keep enforcement points trustworthy.
     - Deliverable 1

   * - 4
     - Requirements for including legacy systems in remote attestation (Technical Specification)
     - How legacy services benefit through credentials issued after a successful appraisal and valid no longer than the appraisal, which trust is lost on the way, and what issuers must meet.
     - Deliverable 1

6. Milestones
-------------

..
   MANDATORY

   AUTHOR GUIDANCE:

   Define dated, checkable milestones aligned with the FG-TIDA meeting
   calendar.

   Typical milestones include:

   - first draft available;
   - WG agreement;
   - submission to the FG-TIDA plenary.

   Keep dates realistic.

   Milestones may be updated without rechartering when the scope itself has
   not changed.

   Do not set dates beyond the lifetime of the Focus Group.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Target date
     - Milestone

   * - 2026-12 (Paris)
     - Charter agreed and white paper outline proposed as working draft.

   * - 2027-01 (Geneva)
     - First draft of Deliverable 1 and outlines of Deliverables 2 to 4.

   * - TBD (3rd FG-TIDA meeting)
     - Deliverable 1 agreed by the Working Group, first drafts of Deliverables 2 to 4.

   * - TBD (within the FG-TIDA lifetime)
     - Deliverables 1 to 4 submitted to the FG-TIDA plenary in time for SG17.

7. Coordination, Dependencies and Liaisons
------------------------------------------

..
   MANDATORY

   AUTHOR GUIDANCE:

   Identify only organizations or groups with a real dependency.

   Include, where relevant:

   - other FG-TIDA Working Groups;
   - ITU-T SG17 Questions;
   - other ITU-T groups;
   - external standards-development organizations;
   - industry or research communities.

   State briefly what the coordination concerns.

   Do not imply that a formal liaison or agreement exists unless one has
   actually been established.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Group / Organization
     - Coordination or dependency

   * - Other FG-TIDA Working Groups
     - Interfaces on authorization, action records, agent identity, terminology and use cases.

   * - ITU-T SG17 Q16/17 (AI security)
     - Agent runtime security, a likely recipient of Deliverables 2 and 3.

   * - ITU-T SG17 Q10/17 (identity management)
     - Proposed continuous checking of agent operation, to align with Deliverable 2.

   * - ITU-T SG17 Q2/17, Q4/17 and Q6/17
     - Zero trust, assurance, and IoT and industrial systems, relevant to Deliverables 3 and 4.

   * - IETF Remote Attestation Procedures (RATS) Working Group
     - Architecture, terms and formats to build on, possible agent profiles of them, reported gaps, review of Deliverables 2 to 4.

   * - TCG, Confidential Computing Consortium, GlobalPlatform, W3C
     - Remote attestation building blocks, credential bridges, and manifests that describe agents.

8. Security and Privacy Considerations
--------------------------------------

..
   OPTIONAL - RECOMMENDED

   AUTHOR GUIDANCE:

   Provide a short paragraph identifying the security and privacy
   concerns that the WG's deliverables must consider.

   Examples may include:

   - impersonation;
   - unauthorized delegation;
   - linkability;
   - surveillance;
   - misuse of identity information;
   - loss of human control;
   - accountability for agent actions.

   Avoid generic disclaimers.

Evidence can reveal sensitive details, so all deliverables address privacy-preserving disclosure: what Evidence reveals, to whom, and how linkable it makes agents and people.
Missing, stale or unverifiable Attestation Results count as a risk, never as a success.
A missing update about an agent calls for fresh Evidence and never demonstrates that nothing changed.

9. Success Criteria and Conclusion
----------------------------------

..
   OPTIONAL

   AUTHOR GUIDANCE:

   State how the WG will know its chartered work is complete.

   Examples include:

   - all deliverables submitted to the FG-TIDA plenary;
   - findings transferred to the relevant SG17 Question;
   - no remaining chartered deliverables.

   Do not describe future approval by SG17 as guaranteed.

The chartered work is complete when all four deliverables are submitted to the FG-TIDA plenary.
They then go to SG17 through FG-TIDA, with Deliverables 2 to 4 as base material, and may inform other standards bodies.

10. Revision History
--------------------

..
   MANDATORY

   AUTHOR GUIDANCE:

   Update this table whenever the scope or charter text changes.

   Changes to milestones alone may be managed separately where appropriate.

.. list-table::
   :header-rows: 1
   :widths: 18 22 60

   * - Version
     - Date
     - Change

   * - 0.4
     - 2026-10-29
     - First draft of the charter
