"""Regression checks for role-scoped GPT-6 execution and obsolete routing bans."""
import unittest
from pathlib import Path
from scripts.test_validate_skill_routing import load_validator

ROOT = Path(__file__).resolve().parents[1]


class GPT6RoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.core = (ROOT / 'skills/project-lead/SKILL.md').read_text()
        cls.validator = load_validator()

    def codes(self, text):
        return {e.code for e in self.validator.validate_text(self.core + '\n' + text)}

    def test_sol_can_implement(self):
        for text in ('Use GPT-6 Sol to execute a bounded implementation task.',
                     'Route this executor task to gpt-6-sol medium.'):
            self.assertNotIn('sol-executor-route', self.codes(text))

    def test_luna_executor_can_modify_owned_code(self):
        for text in ('The authorized GPT-6 Luna executor may write code within its owned scope.',
                     'The gpt-6-luna executor may call mutating tools within its owned scope.'):
            self.assertNotIn('luna-authority', self.codes(text))

    def test_luna_helper_cannot_gain_mutation_from_name(self):
        for text in ('The read-only Luna assistant may write code.',
                     'The Luna information helper may call mutating tools.',
                     'The Luna executor may accept its own work.'):
            self.assertIn('luna-authority', self.codes(text))

    def test_legacy_luna_stays_read_only(self):
        self.assertIn('luna-authority', self.codes(
            'The gpt-5.6-luna executor may write code within its owned scope.'))
        self.assertIn('sol-executor-route', self.codes(
            'Use gpt-5.6-sol to execute a bounded implementation task.'))

    def test_information_assistant_is_legacy_only(self):
        reference = (ROOT / 'skills/project-lead/references/luna-information-assistance.md').read_text()
        self.assertIn('using only an available authorized `gpt-5.6-luna` route', reference)
        self.assertIn('do not substitute `gpt-6-luna`', reference)
        self.assertNotIn('using an available authorized `gpt-6-luna`', reference)

    def test_retired_model_absent_from_active_skill_and_readmes(self):
        paths = list((ROOT / 'skills/project-lead').rglob('*.md'))
        paths += [ROOT / 'README.md', ROOT / 'README.zh-CN.md']
        for path in paths:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertNotRegex(path.read_text().lower(), r'\b(?:spark|terra)\b')

    def test_retired_model_rejected_in_operational_references(self):
        reference = ROOT / 'skills/project-lead/references/model-routing.md'
        for statement in ('Use gpt-5.3-codex-spark for this task.',
                          'Spark remains a compatibility executor.',
                          'Use gpt-5.6-terra for this task.',
                          'Terra remains a compatibility executor.'):
            errors = self.validator.validate_operational_reference_text(
                reference.name, reference.read_text() + '\n' + statement)
            self.assertIn('retired-model', {error.code for error in errors})

    def test_table_rows_do_not_share_permissions(self):
        self.assertNotIn('luna-authority', self.codes(
            '| GPT-6 Sol | may independently review |\n'
            '| GPT-6 Luna | formal implementation |'))

    def test_obsolete_blanket_roles_are_rejected(self):
        for text in ('Sol remains reserved for controller work and independent review.',
                     'Luna is always read-only regardless of task role.',
                     'All execution tasks must use Sol low.',
                     'Always use Luna medium for every task.'):
            self.assertIn('obsolete-routing', self.codes(text))


if __name__ == '__main__':
    unittest.main()
