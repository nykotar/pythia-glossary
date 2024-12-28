# Contributing to Pythia Glossary

Thank you for your interest in contributing to the Pythia Glossary! There are a couple of ways you can contribute to this project:

1. Suggesting terms or revisions
2. Making direct edits

To suggest a new term or update an existing one, you can either [open an issue](https://github.com/nykotar/pythia-glossary/issues/new) or join the conversation on our Discord.

The rest of this guide will talk about how to contribute directly.

---

## **How the Glossary Works**

The glossary is built using YAML files stored in the `terms` directory. Each file represents one term and follows a simple structure:

```yaml
name: The primary term
aliases:
  - Acronym
  - Synonym
definition: |
  Definition here.
```
  
Example:
```yaml
name: Chair
aliases:
  - Seat
  - Armchair
  - Recliner
definition: |
  A piece of furniture designed for sitting, typically consisting of a backrest, seat, and legs, often with armrests.
```

---

## Guidelines for Adding or Updating Terms

### 1. **File Structure**
- **File Name**: The file name should match the term’s primary name in lowercase, with spaces replaced by underscores (e.g., `controlled_remote_viewing.yaml`).
- **Directory**: Place all term files in the `terms` directory.

### 2. **Definition Best Practices**
- Keep definitions **short and focused** (1-2 paragraphs is ideal).
- Ensure accuracy and consistency by including reliable **sources** if available.
- Add any **related resources** if necessary (e.g., articles, books).

### 3. **Aliases**
- Use the `aliases` field to list any alternative names or abbreviations for the term.
- If there are no aliases, leave the field as an empty list: `aliases: []`.

---

## Step-by-Step Contribution Guide

### If You’re New to Git/GitHub

1. **Create a GitHub Account** (if you don’t already have one).
   - Visit [GitHub](https://github.com/) and sign up.

2. **Fork the Repository**
   - Click the “Fork” button on the project’s main page to create your own copy of the repository.

3. **Edit Files Directly on GitHub**
   - Navigate to the `terms` directory in your forked repository.
   - Click “Add file” > “Create new file”.
   - Name your file using the term’s primary name (e.g., `psi_target.yaml`).
   - Add the YAML content for the term.

4. **Submit a Pull Request**
   - After saving your changes, click “Pull requests” on the original project’s page.
   - Select “New pull request” and follow the prompts to propose your changes.

### If You’re Familiar with Git/GitHub

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nykotar/pythia-glossary.git
   cd pythia-glossary
   ```

2. **Create a New Branch**
   ```bash
   git checkout -b add-term-<term-name>
   ```

3. **Add or Update YAML Files**
   - Create or edit files in the `terms` directory.
   - Follow the structure outlined above.

4. **Commit and Push Your Changes**
   ```bash
   git add terms/<file-name>.yaml
   git commit -m "Add term: <term-name>"
   git push origin add-term-<term-name>
   ```

5. **Open a Pull Request**
   - Visit your forked repository on GitHub.
   - Click “Compare & pull request” and submit your changes for review.

---

## **Need Help?**

If you have any questions feel free to ask in the Discord server.
