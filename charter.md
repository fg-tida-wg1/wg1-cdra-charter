# FG-TIDA WG1: Continuous and Dynamic Remote Attestation for Agentic AI (CDRA)

## Charter Information

|||
|-|-|
|Charter version|0.5|
|Date|2026-11-03|
|Status|Draft, initial proposal for discussion|

## 1\. Group Information

|Field|Content|
|-|-|
|Working group name and acronym|Continuous and Dynamic Remote Attestation for Agentic AI (CDRA), working title, presented as Remote Attestation for Agentic AI (RA-AAI)|
|Basis|RA-AAI roadmap v1.0, presented at the FG-TIDA preparation meeting of 30 September 2026|
|FG-TIDA theme(s) covered|Clauses 4.2 to 4.5 of the FG-TIDA Terms of Reference, with Annex A examples A.1.1, A.1.4, A.2.1, A.2.2, A.2.7 and A.2.8|
|Chair(s) / co-chairs|TBD|
|Editor(s) of the main deliverables|TBD|
|Theme proposers|Henk Birkholz, Houda Labiod (Huawei)|
|Mailing list|TBD|
|Repository and issue tracker|https://github.com/fg-tida-wg1/wg1-cdra-charter|
|Working methods|Consensus as in the FG-TIDA Terms of Reference, co-chairs, empowered editors, bi-weekly calls, and workshops or webinars where useful|
|Charter status and version|Draft 0.5|

## 2\. Background and Problem Statement

AI agents plan, invoke tools, execute tasks locally or remotely through inter-agent collaboration, and interact with any real-time environment while reducing direct human control over internal decision-making logic.

Before a service releases a payment, a secret or access to a production system to an agent, it needs to know continuously what is actually being executed.

Today, services obtain this information about platforms through remote attestation procedures, in the form of snapshots.
An Attester produces Evidence about its state, and a Verifier appraises that Evidence and issues Attestation Results.
This works well for systems that are checked once at start and then stay (mostly) the same.
Using Evidence from such snapshots, a Verifier can determine what code is running where, but not what an agent's context or intent actually is.

Agentic AI systems pose the following challenges for remote attestation, grouped into three core questions.

* What to attest (measure): AI agents are dynamic composites of model, code, tools, policies and a context of instructions, data and memory, and any part can change at runtime.
  Remote attestation of such changing parts is called dynamic attestation in this charter.
  AI agents expand the surface of trust for which remote attestation was designed.
  The platform, the runtime environment, the model, the tools, the policy, the identity, and the behaviour must all be attested, not just the hardware state at boot.
* How to attest (appraise and act): each service enforces its own rules on Attestation Results, and agents rely on other agents when they delegate.
  Many legacy services can neither produce Evidence nor read Attestation Results.
* When to attest (refresh): a check at an agent's start-up is not enough to demonstrate the trustworthiness of its next action.
  Therefore, Evidence and Attestation Results about a set of related agents have to flow continuously.
  Remote attestation with such a continuous flow is called continuous attestation in this charter.

## 3\. Goals

The Working Group enables dynamic attestation and continuous attestation for AI agents that evolve during their execution, with the associated flow of Attestation Results as one input to enforcement.

Its pre-standardization work builds on existing specifications toward open, interoperable and privacy-preserving remote attestation, so that users and services can decide whether to consider an agent trustworthy, independent of where the agent runs.

The Working Group describes what to measure, how to appraise and act, and when to refresh, and maps existing building blocks and remaining gaps (Deliverable 1).

* What: The Working Group specifies requirements for Evidence about an agent's dynamically changing parts, which Verifiers appraise against Reference Values from a signed manifest of its intended parts (Deliverable 2).
* How: The Working Group describes an architecture model of layered Attesters and Verifiers (Deliverable 3) and the technical governance of trust domains with changing composition (Deliverable 6).
  It specifies requirements on Attestation Results as one input to enforcement by policy or by technology (Deliverable 2), the inclusion of legacy systems (Deliverable 5) and, if FG-TIDA management confirms this item, the conveyance of Evidence and Attestation Results in agent interactions (Deliverable 4).
* When: The Working Group specifies requirements for keeping Evidence and Attestation Results continuously fresh, with triggers keyed to risk (Deliverable 2).

## 4\. Scope and Non-Goals

### In Scope

* What: Evidence about an agent's parts and context, and about its behaviour where an Attesting Environment measures it, as these change at runtime.
* What: Evidence about all agents, tools and models in one task, appraised as one composition.
* What: Signed self-assertions such as manifests, build statements or operator logs, which Verifiers keep apart from Evidence and use at most as Endorsements or Reference Values.
* How: Different remote attestation schemes, with existing continuous schemes augmented and dynamic schemes added, in an architecture of layered Attesters and Verifiers.
* How: Appraisal of Evidence by Verifiers and of Attestation Results by Relying Parties in steps that can be tested one by one, with distinguishable failure classes and negative test cases.
* How: Attestation Results with a trustworthiness tier per aspect of an agent, such as its configuration, executables or hardware, instead of a single pass or fail.
* How: Attestation Results as one input to enforcement, also when stale, missing, negative or incomplete, and Evidence about the enforcement points.
* How: Binding Evidence to an agent's platform and identity, and privacy-preserving disclosure of Evidence and Attestation Results.
* How: An interoperability model for legacy systems that cannot produce Evidence or read Attestation Results, such as credentials issued only on accepted Attestation Results and valid no longer than the underlying Attestation Results, with interfaces to identification formats.
* How: If FG-TIDA management confirms this item, extensions and profiles of existing agent interaction protocols to discover and convey Evidence and Attestation Results, and to distinguish agent-to-agent interactions unambiguously from interactions in remote attestation procedures.
* How: Secure technical governance of trust domains whose composition changes continuously, taking into account challenges such as intent deterioration.
* When: Risk-keyed triggers for fresh Evidence and new appraisals, such as elapsed time, restarts, tool calls, delegation and changes to an agent's parts, and how long Attestation Results about a set of related agents stay valid.
* When: Fresh Evidence at each stage of an agent's lifecycle, from first deployment through changes to its capabilities to retirement.

### Out of Scope / Non-Goals

The Working Group does not specify complete protocols, but describes architectures, interaction models and information models for messages.
It does not define new languages, core protocols such as CoAP, protocol messages or document formats, including those for Evidence, Attestation Results and appraisal policies, but extends existing specifications only.
It addresses governance only as technical governance of trust domains, not AI governance, liability or jurisdiction.
It does not decide on individual agent actions, on the validity of authorizations or on privileges, and states requirements on Attestation Results, which are one input to such decisions.
It does not define agent identifiers, new hardware or training data provenance, and does not register, certify or benchmark agents or evaluate their security.
It uses statements about training data provenance only as input to appraisal, at most as Endorsements.

## 5\. Programme of Work and Deliverables

|#|Deliverable|Short description|Input documents|
|-|-|-|-|
|1|White paper: Remote Attestation Challenges for Agentic AI Systems (Technical Report)|What to measure, how to appraise and act, and when to refresh, with threats, state of the art, building blocks and gaps.|WG1 white paper outline (September 2026), RA-AAI roadmap v1.0|
|2|Requirements for continuous and dynamic remote attestation of agentic AI systems (Technical Specification)|What Evidence about an agent's changing parts contains, how Verifiers appraise it against Reference Values from a signed manifest, when fresh Evidence is due, how long Attestation Results stay valid, and their trustworthiness tiers per aspect as one input to enforcement.|Deliverable 1, RA-AAI roadmap v1.0|
|3|Architecture model for multi-layered remote attestation of agentic AI systems (Technical Report)|Building blocks and data flows for layered Attesters and Verifiers, the integration of standardized and emerging layering models, and message semantics for new roles, documents and governance.|Deliverable 1|
|4|Integration of remote attestation into agent interaction protocols (Technical Specification)|If FG-TIDA management confirms this item, extensions and profiles of existing agent interaction protocols to discover and convey Evidence and Attestation Results, with privacy-preserving methods.|Deliverables 1 and 3|
|5|Interoperability model for including legacy systems in remote attestation (Technical Specification)|Credentials based on accepted Attestation Results, the information such credentials do not convey, issuer requirements, and interfaces to identification formats such as SPIFFE/SPIRE, X.509v3, PKIX, CWT certificates and DIDs.|Deliverable 1|
|6|Technical governance of trust domains with changing composition (Technical Report)|Integration and extension of existing governance models for the secure technical governance of trust domains whose composition changes continuously.|Deliverables 1 and 3|

## 6\. Milestones

|Target date|Milestone|
|-|-|
|2026-12 (Paris)|Charter agreed and white paper outline proposed as working draft.|
|2027-01 (Geneva)|First draft of Deliverable 1 and outlines of Deliverables 2 to 6.|
|TBD (3rd FG-TIDA meeting)|Deliverable 1 agreed by the Working Group, first drafts of Deliverables 2 to 6.|
|TBD (within the FG-TIDA lifetime)|Deliverables 1 to 6 submitted to the FG-TIDA plenary in time for SG17.|

## 7\. Coordination, Dependencies and Liaisons

|Group / Organization|Coordination or dependency|
|-|-|
|FG-TIDA WG0 (Use Cases and Terminology)|Use cases and terminology, including the terms of IETF RFC 9334 and those this charter introduces.|
|FG-TIDA WG2 (Identity, Behaviour and Enforcement for AI Agents)|Enforcement, with Attestation Results from WG1 as one of the inputs to WG2.|
|Other FG-TIDA Working Groups|Interfaces on authorization, action records and agent identity.|
|ITU-T SG17 Q16/17 (AI security)|Agent runtime security, a likely recipient of Deliverables 2 and 3.|
|ITU-T SG17 Q16/17, XSTR.aam (AI accountability manifest)|Operator-declared intent and scope of agents, complemented by Evidence about their actual state.|
|ITU-T SG17 Q10/17 (identity management)|Proposed XSTR.caars on continuous checking of autonomous agent operation against a versioned rule set, to align with Deliverable 2.|
|ITU-T SG17 Q2/17, Q4/17 and Q6/17|Zero trust, assurance, and IoT and industrial systems, relevant to Deliverables 2 and 5.|
|IETF Remote Attestation Procedures (RATS) Working Group|Architecture, terms and formats to build on, possible agent profiles of them, reported gaps, and review of Deliverables 2 to 5.|
|TCG, Confidential Computing Consortium, GlobalPlatform, W3C|Remote attestation building blocks, credential bridges, and manifests that describe agents.|

## 8\. Security and Privacy Considerations

Evidence and Attestation Results can contain sensitive information about agents and the people they act for.
All deliverables address what is disclosed to which party, how linkable agents and people become, and what a party learns from a failed appraisal.
Missing, stale or unverifiable Attestation Results are a risk, and the absence of an update about an agent does not indicate that its state is unchanged.

## 9\. Success Criteria and Conclusion

The chartered work of the Working Group ends when all six deliverables are close to completion and the FG-TIDA plenary approves them by consensus.
FG-TIDA then dispatches the deliverables to SG17, its parent group, and through liaison statements to other standards bodies and industry consortia, such as the IETF, TCG, GlobalPlatform, the Confidential Computing Consortium and W3C.
SG17 and these bodies can complete the standardization, for example with ITU-T Recommendations.

## 10\. Revision History

|Version|Date|Change|
|-|-|-|
|0.4|2026-10-29|First draft of the charter|
|0.5|2026-11-03|Six deliverables instead of four, interfaces to WG0 and WG2, terminology aligned with IETF RFC 9334, two terms introduced|
