# Optional Teaching and Lecturer Track

**Author:** [@kwis7](https://github.com/kwis7)

This optional track turns the same local-first principles into a reusable course workspace. It is intentionally generic: adapt it to institutional policies, accessibility requirements, assessment rules, and student-data protections.

## Course agent layout

```text
Teaching-Agent/
└── courses/
    └── COURSE-CODE-course-title/
        ├── course-profile.md
        ├── 01-course-design/
        │   ├── learning-outcomes/
        │   ├── syllabus/
        │   └── policies/
        ├── 02-weekly-materials/
        │   └── week-01-topic/
        │       ├── student-materials/
        │       ├── instructor-notes/
        │       └── readings/
        ├── 03-assessment/
        │   └── assignment-01/
        │       ├── brief/
        │       ├── rubric/
        │       ├── benchmark-samples/
        │       └── feedback-templates/
        ├── secured_data/          # private; ignored by Git
        ├── workspace/
        └── outputs/
```

Copy the [course-agent template](../templates/course-agent/) before adding a real course. The template includes README files rather than actual student work or benchmark essays.

## Why the levels matter

- **Student materials** are what can be distributed.
- **Instructor notes** contain facilitation plans, anticipated misconceptions, and internal preparation.
- **Readings** are arranged by week or section so the agent does not confuse material from different parts of the course.
- **Assessment components** have their own briefs, rubrics, benchmark-sample notes, and feedback conventions.
- **Secured data** is distinct from all of the above and is never a shared knowledge base.

## Assisted grading: a protected workflow

AI assistance cannot replace an instructor's accountability. It should never make final grade decisions automatically or upload student work without explicit institutional approval. If your policy permits support, use this constrained flow:

1. Put the approved brief, rubric, criteria, and anonymised benchmark notes in the assessment folder.
2. Place submissions in `secured_data/submissions/`, excluded from Git and from general course context.
3. Create one isolated task context per submission. Load only that submission plus the authorised reference files.
4. Ask for an evidence-linked provisional score rationale and specific feedback, not a final recorded grade.
5. Review the rationale yourself, check consistency and bias, then decide and record the grade through your authorised process.
6. Save only the reviewed feedback output where your policy permits; do not mix one student's work into another student's task context.

This one-at-a-time design helps prevent one student's answer from influencing the treatment of another and keeps the evaluator's context bounded.

## A generic course-build prompt

```text
Create a course workspace from the course-agent template. First ask for course
title, level, learning outcomes, weekly structure, assessment components,
institutional policies, and accessibility needs. Then show the proposed tree.
After confirmation, create empty folders and README files only. Keep student
materials separate from instructor notes. Do not generate or import student
data. For each assessment, create placeholders for the brief, rubric, criteria,
benchmark-sample notes, and feedback template.
```

## A generic grading-review prompt

```text
For this one submission only, read the named assignment brief, rubric, criteria,
and permitted benchmark notes. Analyse the work against each criterion, quote or
describe evidence from the submission, identify uncertainty, and propose a
provisional band with constructive feedback. Do not compare this submission with
other student submissions. Do not make the final grade decision or write it to
an official system. Flag any policy, accessibility, academic-integrity, or bias
concern for instructor review.
```
