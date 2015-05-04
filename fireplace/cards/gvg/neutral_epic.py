from ..utils import *


##
# Minions

# Hobgoblin
class GVG_104:
	events = [
		OWN_MINION_PLAY.on(
			lambda self, player, card, *args: card.atk == 1 and [Buff(card, "GVG_104a")] or []
		)
	]


# Piloted Sky Golem
class GVG_105:
	def deathrattle(self):
		return [Summon(CONTROLLER, randomCollectible(type=CardType.MINION, cost=4))]


# Junkbot
class GVG_106:
	events = [
		Death(FRIENDLY + MECH).on(Buff(SELF, "GVG_106e"))
	]


# Enhance-o Mechano
class GVG_107:
	def action(self):
		for target in self.controller.field:
			tag = random.choice((GameTag.WINDFURY, GameTag.TAUNT, GameTag.DIVINE_SHIELD))
			yield SetTag(target, {tag: True})


# Recombobulator
class GVG_108:
	def action(self, target):
		choice = randomCollectible(type=CardType.MINION, cost=target.cost)
		return [Morph(TARGET, choice)]


# Clockwork Giant
class GVG_121:
	def cost(self, value):
		return value - len(self.controller.opponent.hand)
