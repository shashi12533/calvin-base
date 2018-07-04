
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightUNOTAND APPLY AT COLON COMMA COMPONENT DEFINE DOCSTRING DOT EQ FALSE GROUP GT IDENTIFIER LBRACE LBRACK LPAREN NULL NUMBER OR RARROW RBRACE RBRACK RPAREN RULE SLASH STRING TRUE UNOT VOIDPORTscript : opt_constdefs opt_compdefs opt_programempty : opt_constdefs : constdefs\n                         | emptyconstdefs : constdefs constdef\n                     | constdefconstdef : DEFINE identifier EQ argumentopt_compdefs : compdefs\n                        | emptycompdefs : compdefs compdef\n                    | compdefcompdef : COMPONENT qualified_name LPAREN opt_argnames RPAREN opt_argnames RARROW opt_argnames LBRACE docstring comp_statements RBRACEdocstring : DOCSTRING\n                     | emptycomp_statements : comp_statements comp_statement\n                           | comp_statementcomp_statement : assignment\n                          | port_property\n                          | internal_port_property\n                          | linkopt_program : program\n                       | emptyprogram : program statement\n                   | statement statement : assignment\n                     | port_property\n                     | link\n                     | define_rule\n                     | group\n                     | applyassignment : IDENTIFIER COLON qualified_name LPAREN named_args RPARENopt_direction : LBRACK IDENTIFIER RBRACK\n                         | emptyport_property : qualified_port opt_direction LPAREN named_args RPARENinternal_port_property : unqualified_port opt_direction LPAREN named_args RPARENlink : void GT voidlink : real_outport GT void\n                | void GT real_inport_list\n                | real_outport GT inport_list\n                | implicit_outport GT inport_list\n                | internal_outport GT inport_listvoid : VOIDPORTinport_list : inport_list COMMA inport\n                       | inportreal_inport_list : inport_list COMMA real_inport\n                       | real_inportinport : real_or_internal_inport\n                  | transformed_inporttransformed_inport : port_transform real_or_internal_inportimplicit_outport : argument\n                            | label argumentreal_or_internal_inport : real_inport\n                                   | internal_inportopt_tag : AT tag_value\n                   | emptytag_value : NUMBER\n                     | STRINGreal_inport : opt_tag qualified_portreal_outport : qualified_portinternal_inport : unqualified_portinternal_outport : unqualified_portport_transform : SLASH argument SLASH\n                          | SLASH label argument SLASHqualified_port : IDENTIFIER DOT IDENTIFIERunqualified_port : DOT IDENTIFIERlabel : COLON identifiernamed_args : named_args named_arg COMMA\n                      | named_args named_arg\n                      | emptynamed_arg : identifier EQ argumentargument : value\n                    | identifieropt_argnames : argnames\n                           | emptyargnames : argnames COMMA IDENTIFIER\n                    | IDENTIFIERidentifiers : identifiers COMMA identifier\n                       | identifieridentifier : IDENTIFIERstring : STRING\n                  | string STRINGvalue : dictionary\n                 | array\n                 | bool\n                 | null\n                 | NUMBER\n                 | stringbool : TRUE\n                | FALSEnull : NULLdictionary : LBRACE members RBRACEmembers : members member COMMA\n                   | members member\n                   | emptymember : string COLON valuevalues : values value COMMA\n                  | values value\n                  | emptyarray :  LBRACK values RBRACKqualified_name : qualified_name DOT IDENTIFIER\n                          | IDENTIFIERdefine_rule : RULE identifier COLON rulerule : rule AND rule\n                | rule OR rulerule : UNOT rulerule : LPAREN rule RPARENrule : identifier\n                | predicatepredicate : identifier LPAREN named_args RPARENapply : APPLY identifiers COLON rulegroup : GROUP identifier COLON identifiers'
    
_lr_action_items = {'COMPONENT':([0,2,3,4,5,8,10,12,14,33,41,42,43,44,45,46,47,50,51,52,53,54,75,82,110,113,186,],[-2,11,-3,-4,-6,11,-11,-5,-79,-72,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,-10,-81,-7,-91,-99,-12,]),'IDENTIFIER':([0,2,3,4,5,6,7,8,9,10,11,12,14,16,18,19,20,21,22,23,24,26,32,33,34,35,36,37,39,41,42,43,44,45,46,47,50,51,52,53,54,57,58,59,60,61,63,65,66,67,68,72,73,75,80,81,82,84,85,87,88,90,91,92,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,120,121,122,124,125,127,128,129,130,132,133,134,135,136,137,138,139,140,141,145,146,147,148,149,151,152,153,155,156,157,158,163,164,165,166,167,168,169,170,171,172,173,175,176,177,178,179,180,181,182,183,184,186,187,189,190,191,],[-2,-2,-3,-4,-6,14,25,-8,-9,-11,56,-5,-79,25,-24,-25,-26,-27,-28,-29,-30,14,14,-72,14,14,73,-42,14,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,-10,14,-23,56,84,-66,86,-2,-2,-2,-2,-78,-65,-81,118,119,-7,-64,-2,-36,-38,-46,-44,126,-47,-48,-55,-53,-2,-60,14,-37,-39,-52,-40,-41,14,14,14,14,-91,-99,-2,14,-69,-2,-58,-54,-56,-57,-49,14,-2,-107,-102,14,14,-108,-111,-110,-77,118,162,14,-34,-68,-45,-43,-62,-2,14,14,-105,-31,-67,14,-63,14,-103,-104,-106,118,-70,-109,-2,25,-13,-14,25,-16,-17,-18,-19,-20,-12,-15,-2,14,-35,]),'RULE':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,33,37,41,42,43,44,45,46,47,50,51,52,53,54,58,72,73,75,82,84,87,88,90,91,93,94,97,99,101,102,103,104,105,110,113,125,130,134,135,138,139,140,141,148,151,152,158,163,168,169,170,173,186,],[-2,-2,-3,-4,-6,32,-8,-9,-11,-5,-79,32,-24,-25,-26,-27,-28,-29,-30,-72,-42,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,-10,-23,-78,-65,-81,-7,-64,-36,-38,-46,-44,-47,-48,-53,-60,-37,-39,-52,-40,-41,-91,-99,-58,-49,-107,-102,-108,-111,-110,-77,-34,-45,-43,-105,-31,-103,-104,-106,-109,-12,]),'GROUP':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,33,37,41,42,43,44,45,46,47,50,51,52,53,54,58,72,73,75,82,84,87,88,90,91,93,94,97,99,101,102,103,104,105,110,113,125,130,134,135,138,139,140,141,148,151,152,158,163,168,169,170,173,186,],[-2,-2,-3,-4,-6,34,-8,-9,-11,-5,-79,34,-24,-25,-26,-27,-28,-29,-30,-72,-42,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,-10,-23,-78,-65,-81,-7,-64,-36,-38,-46,-44,-47,-48,-53,-60,-37,-39,-52,-40,-41,-91,-99,-58,-49,-107,-102,-108,-111,-110,-77,-34,-45,-43,-105,-31,-103,-104,-106,-109,-12,]),'APPLY':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,33,37,41,42,43,44,45,46,47,50,51,52,53,54,58,72,73,75,82,84,87,88,90,91,93,94,97,99,101,102,103,104,105,110,113,125,130,134,135,138,139,140,141,148,151,152,158,163,168,169,170,173,186,],[-2,-2,-3,-4,-6,35,-8,-9,-11,-5,-79,35,-24,-25,-26,-27,-28,-29,-30,-72,-42,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,-10,-23,-78,-65,-81,-7,-64,-36,-38,-46,-44,-47,-48,-53,-60,-37,-39,-52,-40,-41,-91,-99,-58,-49,-107,-102,-108,-111,-110,-77,-34,-45,-43,-105,-31,-103,-104,-106,-109,-12,]),'VOIDPORT':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,33,37,41,42,43,44,45,46,47,50,51,52,53,54,58,65,66,72,73,75,82,84,87,88,90,91,93,94,97,99,101,102,103,104,105,110,113,125,130,134,135,138,139,140,141,148,151,152,158,163,168,169,170,173,175,176,177,178,179,180,181,182,183,184,186,187,191,],[-2,-2,-3,-4,-6,37,-8,-9,-11,-5,-79,37,-24,-25,-26,-27,-28,-29,-30,-72,-42,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,-10,-23,37,37,-78,-65,-81,-7,-64,-36,-38,-46,-44,-47,-48,-53,-60,-37,-39,-52,-40,-41,-91,-99,-58,-49,-107,-102,-108,-111,-110,-77,-34,-45,-43,-105,-31,-103,-104,-106,-109,-2,37,-13,-14,37,-16,-17,-18,-19,-20,-12,-15,-35,]),'COLON':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,25,33,37,41,42,43,44,45,46,47,50,51,52,53,54,58,69,70,71,72,73,75,82,84,87,88,90,91,93,94,97,99,100,101,102,103,104,105,110,112,113,125,130,134,135,138,139,140,141,148,151,152,158,163,168,169,170,173,175,176,177,178,179,180,181,182,183,184,186,187,191,],[-2,-2,-3,-4,-6,26,-8,-9,-11,-5,-79,26,-24,-25,-26,-27,-28,-29,-30,59,-72,-42,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,-10,-23,106,107,108,-78,-65,-81,-7,-64,-36,-38,-46,-44,-47,-48,-53,-60,26,-37,-39,-52,-40,-41,-91,143,-99,-58,-49,-107,-102,-108,-111,-110,-77,-34,-45,-43,-105,-31,-103,-104,-106,-109,-2,26,-13,-14,26,-16,-17,-18,-19,-20,-12,-15,-35,]),'DOT':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,25,33,37,41,42,43,44,45,46,47,50,51,52,53,54,55,56,58,65,66,67,68,72,73,75,82,83,84,87,88,90,91,93,94,97,98,99,101,102,103,104,105,110,113,119,124,125,126,130,133,134,135,138,139,140,141,148,151,152,153,158,163,166,168,169,170,173,175,176,177,178,179,180,181,182,183,184,186,187,191,],[-2,-2,-3,-4,-6,36,-8,-9,-11,-5,-79,36,-24,-25,-26,-27,-28,-29,-30,60,-72,-42,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,-10,81,-101,-23,36,36,36,36,-78,-65,-81,-7,81,-64,-36,-38,-46,-44,-47,-48,-53,36,-60,-37,-39,-52,-40,-41,-91,-99,-100,36,-58,60,-49,36,-107,-102,-108,-111,-110,-77,-34,-45,-43,-62,-105,-31,-63,-103,-104,-106,-109,-2,36,-13,-14,36,-16,-17,-18,-19,-20,-12,-15,-35,]),'NUMBER':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,33,37,39,41,42,43,44,45,46,47,49,50,51,52,53,54,57,58,61,72,73,75,78,79,82,84,87,88,90,91,93,94,95,97,99,100,101,102,103,104,105,110,113,114,125,130,132,134,135,138,139,140,141,143,144,148,151,152,158,163,165,168,169,170,173,175,176,177,178,179,180,181,182,183,184,186,187,191,],[-2,-2,-3,-4,-6,46,-8,-9,-11,-5,-79,46,-24,-25,-26,-27,-28,-29,-30,-72,-42,46,-71,-82,-83,-84,-85,-86,-87,-2,-88,-89,-90,-80,-10,46,-23,-66,-78,-65,-81,46,-98,-7,-64,-36,-38,-46,-44,-47,-48,128,-53,-60,46,-37,-39,-52,-40,-41,-91,-99,-97,-58,-49,46,-107,-102,-108,-111,-110,-77,46,-96,-34,-45,-43,-105,-31,46,-103,-104,-106,-109,-2,46,-13,-14,46,-16,-17,-18,-19,-20,-12,-15,-35,]),'LBRACE':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,33,37,39,41,42,43,44,45,46,47,49,50,51,52,53,54,57,58,61,72,73,75,78,79,82,84,87,88,90,91,93,94,97,99,100,101,102,103,104,105,110,113,114,116,117,118,125,130,132,134,135,138,139,140,141,143,144,148,151,152,158,162,163,165,168,169,170,171,173,174,175,176,177,178,179,180,181,182,183,184,186,187,191,],[-2,-2,-3,-4,-6,48,-8,-9,-11,-5,-79,48,-24,-25,-26,-27,-28,-29,-30,-72,-42,48,-71,-82,-83,-84,-85,-86,-87,-2,-88,-89,-90,-80,-10,48,-23,-66,-78,-65,-81,48,-98,-7,-64,-36,-38,-46,-44,-47,-48,-53,-60,48,-37,-39,-52,-40,-41,-91,-99,-97,-73,-74,-76,-58,-49,48,-107,-102,-108,-111,-110,-77,48,-96,-34,-45,-43,-105,-75,-31,48,-103,-104,-106,-2,-109,175,-2,48,-13,-14,48,-16,-17,-18,-19,-20,-12,-15,-35,]),'LBRACK':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,27,33,37,39,41,42,43,44,45,46,47,49,50,51,52,53,54,57,58,61,72,73,75,78,79,82,84,87,88,90,91,93,94,97,99,100,101,102,103,104,105,110,113,114,125,130,132,134,135,138,139,140,141,143,144,148,151,152,158,163,165,168,169,170,173,175,176,177,178,179,180,181,182,183,184,185,186,187,191,],[-2,-2,-3,-4,-6,49,-8,-9,-11,-5,-79,49,-24,-25,-26,-27,-28,-29,-30,63,-72,-42,49,-71,-82,-83,-84,-85,-86,-87,-2,-88,-89,-90,-80,-10,49,-23,-66,-78,-65,-81,49,-98,-7,-64,-36,-38,-46,-44,-47,-48,-53,-60,49,-37,-39,-52,-40,-41,-91,-99,-97,-58,-49,49,-107,-102,-108,-111,-110,-77,49,-96,-34,-45,-43,-105,-31,49,-103,-104,-106,-109,-2,49,-13,-14,49,-16,-17,-18,-19,-20,63,-12,-15,-35,]),'TRUE':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,33,37,39,41,42,43,44,45,46,47,49,50,51,52,53,54,57,58,61,72,73,75,78,79,82,84,87,88,90,91,93,94,97,99,100,101,102,103,104,105,110,113,114,125,130,132,134,135,138,139,140,141,143,144,148,151,152,158,163,165,168,169,170,173,175,176,177,178,179,180,181,182,183,184,186,187,191,],[-2,-2,-3,-4,-6,50,-8,-9,-11,-5,-79,50,-24,-25,-26,-27,-28,-29,-30,-72,-42,50,-71,-82,-83,-84,-85,-86,-87,-2,-88,-89,-90,-80,-10,50,-23,-66,-78,-65,-81,50,-98,-7,-64,-36,-38,-46,-44,-47,-48,-53,-60,50,-37,-39,-52,-40,-41,-91,-99,-97,-58,-49,50,-107,-102,-108,-111,-110,-77,50,-96,-34,-45,-43,-105,-31,50,-103,-104,-106,-109,-2,50,-13,-14,50,-16,-17,-18,-19,-20,-12,-15,-35,]),'FALSE':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,33,37,39,41,42,43,44,45,46,47,49,50,51,52,53,54,57,58,61,72,73,75,78,79,82,84,87,88,90,91,93,94,97,99,100,101,102,103,104,105,110,113,114,125,130,132,134,135,138,139,140,141,143,144,148,151,152,158,163,165,168,169,170,173,175,176,177,178,179,180,181,182,183,184,186,187,191,],[-2,-2,-3,-4,-6,51,-8,-9,-11,-5,-79,51,-24,-25,-26,-27,-28,-29,-30,-72,-42,51,-71,-82,-83,-84,-85,-86,-87,-2,-88,-89,-90,-80,-10,51,-23,-66,-78,-65,-81,51,-98,-7,-64,-36,-38,-46,-44,-47,-48,-53,-60,51,-37,-39,-52,-40,-41,-91,-99,-97,-58,-49,51,-107,-102,-108,-111,-110,-77,51,-96,-34,-45,-43,-105,-31,51,-103,-104,-106,-109,-2,51,-13,-14,51,-16,-17,-18,-19,-20,-12,-15,-35,]),'NULL':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,33,37,39,41,42,43,44,45,46,47,49,50,51,52,53,54,57,58,61,72,73,75,78,79,82,84,87,88,90,91,93,94,97,99,100,101,102,103,104,105,110,113,114,125,130,132,134,135,138,139,140,141,143,144,148,151,152,158,163,165,168,169,170,173,175,176,177,178,179,180,181,182,183,184,186,187,191,],[-2,-2,-3,-4,-6,52,-8,-9,-11,-5,-79,52,-24,-25,-26,-27,-28,-29,-30,-72,-42,52,-71,-82,-83,-84,-85,-86,-87,-2,-88,-89,-90,-80,-10,52,-23,-66,-78,-65,-81,52,-98,-7,-64,-36,-38,-46,-44,-47,-48,-53,-60,52,-37,-39,-52,-40,-41,-91,-99,-97,-58,-49,52,-107,-102,-108,-111,-110,-77,52,-96,-34,-45,-43,-105,-31,52,-103,-104,-106,-109,-2,52,-13,-14,52,-16,-17,-18,-19,-20,-12,-15,-35,]),'STRING':([0,2,3,4,5,7,8,9,10,12,14,16,18,19,20,21,22,23,24,33,37,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,57,58,61,72,73,75,76,77,78,79,82,84,87,88,90,91,93,94,95,97,99,100,101,102,103,104,105,110,111,112,113,114,125,130,132,134,135,138,139,140,141,142,143,144,148,151,152,158,160,163,165,168,169,170,173,175,176,177,178,179,180,181,182,183,184,186,187,191,],[-2,-2,-3,-4,-6,53,-8,-9,-11,-5,-79,53,-24,-25,-26,-27,-28,-29,-30,-72,-42,53,-71,-82,-83,-84,-85,-86,75,-2,-2,-88,-89,-90,-80,-10,53,-23,-66,-78,-65,-81,53,-94,53,-98,-7,-64,-36,-38,-46,-44,-47,-48,129,-53,-60,53,-37,-39,-52,-40,-41,-91,-93,75,-99,-97,-58,-49,53,-107,-102,-108,-111,-110,-77,-92,53,-96,-34,-45,-43,-105,-95,-31,53,-103,-104,-106,-109,-2,53,-13,-14,53,-16,-17,-18,-19,-20,-12,-15,-35,]),'$end':([0,1,2,3,4,5,7,8,9,10,12,14,15,16,17,18,19,20,21,22,23,24,33,37,41,42,43,44,45,46,47,50,51,52,53,54,58,72,73,75,82,84,87,88,90,91,93,94,97,99,101,102,103,104,105,110,113,125,130,134,135,138,139,140,141,148,151,152,158,163,168,169,170,173,186,],[-2,0,-2,-3,-4,-6,-2,-8,-9,-11,-5,-79,-1,-21,-22,-24,-25,-26,-27,-28,-29,-30,-72,-42,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,-10,-23,-78,-65,-81,-7,-64,-36,-38,-46,-44,-47,-48,-53,-60,-37,-39,-52,-40,-41,-91,-99,-58,-49,-107,-102,-108,-111,-110,-77,-34,-45,-43,-105,-31,-103,-104,-106,-109,-12,]),'DEFINE':([0,3,5,12,14,33,41,42,43,44,45,46,47,50,51,52,53,75,82,110,113,],[6,6,-6,-5,-79,-72,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,-81,-7,-91,-99,]),'EQ':([13,14,150,],[57,-79,165,]),'COMMA':([14,33,41,42,43,44,45,46,47,50,51,52,53,71,72,73,75,84,89,90,91,93,94,97,99,102,103,104,105,110,111,113,114,116,118,125,130,139,141,149,151,152,160,162,172,],[-79,-72,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,109,-78,-65,-81,-64,124,-52,-44,-47,-48,-53,-60,133,-52,133,133,-91,142,-99,144,146,-76,-58,-49,109,-77,164,-52,-43,-95,-75,-70,]),'GT':([14,25,27,28,29,30,31,33,37,38,40,41,42,43,44,45,46,47,50,51,52,53,73,74,75,84,110,113,185,],[-79,-79,-59,65,66,67,68,-72,-42,-50,-61,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,-65,-51,-81,-64,-91,-99,-61,]),'SLASH':([14,33,41,42,43,44,45,46,47,50,51,52,53,65,66,67,68,75,110,113,124,131,133,154,],[-79,-72,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,100,100,100,100,-81,-91,-99,100,153,100,166,]),'LPAREN':([14,27,55,56,62,64,73,83,84,106,108,119,123,134,136,137,156,157,185,188,],[-79,-2,80,-101,85,-33,-65,120,-64,137,137,-100,-32,155,137,137,137,137,-2,189,]),'AND':([14,134,135,138,140,158,159,168,169,170,173,],[-79,-107,156,-108,156,-105,156,-103,156,-106,-109,]),'OR':([14,134,135,138,140,158,159,168,169,170,173,],[-79,-107,157,-108,157,-105,157,-103,-104,-106,-109,]),'RPAREN':([14,33,41,42,43,44,45,46,47,50,51,52,53,75,80,85,110,113,115,116,117,118,120,121,122,134,138,147,149,155,158,159,162,164,167,168,169,170,172,173,189,190,],[-79,-72,-71,-82,-83,-84,-85,-86,-87,-88,-89,-90,-80,-81,-2,-2,-91,-99,145,-73,-74,-76,-2,148,-69,-107,-108,163,-68,-2,-105,170,-75,-67,173,-103,-104,-106,-70,-109,-2,191,]),'RBRACE':([37,42,43,44,45,46,47,48,50,51,52,53,73,75,76,77,84,87,88,90,91,93,94,97,99,101,102,103,104,105,110,111,113,125,130,142,148,151,152,160,163,179,180,181,182,183,184,187,191,],[-42,-82,-83,-84,-85,-86,-87,-2,-88,-89,-90,-80,-65,-81,110,-94,-64,-36,-38,-46,-44,-47,-48,-53,-60,-37,-39,-52,-40,-41,-91,-93,-99,-58,-49,-92,-34,-45,-43,-95,-31,186,-16,-17,-18,-19,-20,-15,-35,]),'RBRACK':([42,43,44,45,46,47,49,50,51,52,53,75,78,79,86,110,113,114,144,],[-82,-83,-84,-85,-86,-87,-2,-88,-89,-90,-80,-81,113,-98,123,-91,-99,-97,-96,]),'AT':([65,66,67,68,98,124,133,153,166,],[95,95,95,95,95,95,95,-62,-63,]),'UNOT':([106,108,136,137,156,157,],[136,136,136,136,136,136,]),'RARROW':([116,117,118,145,161,162,],[-73,-74,-76,-2,171,-75,]),'DOCSTRING':([175,],[177,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'script':([0,],[1,]),'opt_constdefs':([0,],[2,]),'constdefs':([0,],[3,]),'empty':([0,2,7,27,48,49,65,66,67,68,80,85,98,120,124,133,145,155,171,175,185,189,],[4,9,17,64,77,79,96,96,96,96,117,122,96,122,96,96,117,122,117,178,64,122,]),'constdef':([0,3,],[5,12,]),'opt_compdefs':([2,],[7,]),'compdefs':([2,],[8,]),'compdef':([2,8,],[10,54,]),'identifier':([6,7,16,26,32,34,35,39,57,100,106,107,108,109,121,132,136,137,147,156,157,165,167,176,179,190,],[13,33,33,61,69,70,72,33,33,33,134,72,134,141,150,33,134,134,150,134,134,33,150,33,33,150,]),'opt_program':([7,],[15,]),'program':([7,],[16,]),'statement':([7,16,],[18,58,]),'assignment':([7,16,176,179,],[19,19,181,181,]),'port_property':([7,16,176,179,],[20,20,182,182,]),'link':([7,16,176,179,],[21,21,184,184,]),'define_rule':([7,16,],[22,22,]),'group':([7,16,],[23,23,]),'apply':([7,16,],[24,24,]),'qualified_port':([7,16,92,176,179,],[27,27,125,27,27,]),'void':([7,16,65,66,176,179,],[28,28,87,101,28,28,]),'real_outport':([7,16,176,179,],[29,29,29,29,]),'implicit_outport':([7,16,176,179,],[30,30,30,30,]),'internal_outport':([7,16,176,179,],[31,31,31,31,]),'argument':([7,16,39,57,100,132,165,176,179,],[38,38,74,82,131,154,172,38,38,]),'label':([7,16,100,176,179,],[39,39,132,39,39,]),'unqualified_port':([7,16,65,66,67,68,98,124,133,176,179,],[40,40,99,99,99,99,99,99,99,185,185,]),'value':([7,16,39,57,78,100,132,143,165,176,179,],[41,41,41,41,114,41,41,160,41,41,41,]),'dictionary':([7,16,39,57,78,100,132,143,165,176,179,],[42,42,42,42,42,42,42,42,42,42,42,]),'array':([7,16,39,57,78,100,132,143,165,176,179,],[43,43,43,43,43,43,43,43,43,43,43,]),'bool':([7,16,39,57,78,100,132,143,165,176,179,],[44,44,44,44,44,44,44,44,44,44,44,]),'null':([7,16,39,57,78,100,132,143,165,176,179,],[45,45,45,45,45,45,45,45,45,45,45,]),'string':([7,16,39,57,76,78,100,132,143,165,176,179,],[47,47,47,47,112,47,47,47,47,47,47,47,]),'qualified_name':([11,59,],[55,83,]),'opt_direction':([27,185,],[62,188,]),'identifiers':([35,107,],[71,139,]),'members':([48,],[76,]),'values':([49,],[78,]),'real_inport_list':([65,],[88,]),'inport_list':([65,66,67,68,],[89,102,104,105,]),'real_inport':([65,66,67,68,98,124,133,],[90,103,103,103,103,151,103,]),'inport':([65,66,67,68,124,133,],[91,91,91,91,152,152,]),'opt_tag':([65,66,67,68,98,124,133,],[92,92,92,92,92,92,92,]),'real_or_internal_inport':([65,66,67,68,98,124,133,],[93,93,93,93,130,93,93,]),'transformed_inport':([65,66,67,68,124,133,],[94,94,94,94,94,94,]),'internal_inport':([65,66,67,68,98,124,133,],[97,97,97,97,97,97,97,]),'port_transform':([65,66,67,68,124,133,],[98,98,98,98,98,98,]),'member':([76,],[111,]),'opt_argnames':([80,145,171,],[115,161,174,]),'argnames':([80,145,171,],[116,116,116,]),'named_args':([85,120,155,189,],[121,147,167,190,]),'tag_value':([95,],[127,]),'rule':([106,108,136,137,156,157,],[135,140,158,159,168,169,]),'predicate':([106,108,136,137,156,157,],[138,138,138,138,138,138,]),'named_arg':([121,147,167,190,],[149,149,149,149,]),'docstring':([175,],[176,]),'comp_statements':([176,],[179,]),'comp_statement':([176,179,],[180,187,]),'internal_port_property':([176,179,],[183,183,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> script","S'",1,None,None,None),
  ('script -> opt_constdefs opt_compdefs opt_program','script',3,'p_script','parser.py',66),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',72),
  ('opt_constdefs -> constdefs','opt_constdefs',1,'p_opt_constdefs','parser.py',76),
  ('opt_constdefs -> empty','opt_constdefs',1,'p_opt_constdefs','parser.py',77),
  ('constdefs -> constdefs constdef','constdefs',2,'p_constdefs','parser.py',82),
  ('constdefs -> constdef','constdefs',1,'p_constdefs','parser.py',83),
  ('constdef -> DEFINE identifier EQ argument','constdef',4,'p_constdef','parser.py',91),
  ('opt_compdefs -> compdefs','opt_compdefs',1,'p_opt_compdefs','parser.py',97),
  ('opt_compdefs -> empty','opt_compdefs',1,'p_opt_compdefs','parser.py',98),
  ('compdefs -> compdefs compdef','compdefs',2,'p_compdefs','parser.py',102),
  ('compdefs -> compdef','compdefs',1,'p_compdefs','parser.py',103),
  ('compdef -> COMPONENT qualified_name LPAREN opt_argnames RPAREN opt_argnames RARROW opt_argnames LBRACE docstring comp_statements RBRACE','compdef',12,'p_compdef','parser.py',111),
  ('docstring -> DOCSTRING','docstring',1,'p_docstring','parser.py',116),
  ('docstring -> empty','docstring',1,'p_docstring','parser.py',117),
  ('comp_statements -> comp_statements comp_statement','comp_statements',2,'p_comp_statements','parser.py',121),
  ('comp_statements -> comp_statement','comp_statements',1,'p_comp_statements','parser.py',122),
  ('comp_statement -> assignment','comp_statement',1,'p_comp_statement','parser.py',129),
  ('comp_statement -> port_property','comp_statement',1,'p_comp_statement','parser.py',130),
  ('comp_statement -> internal_port_property','comp_statement',1,'p_comp_statement','parser.py',131),
  ('comp_statement -> link','comp_statement',1,'p_comp_statement','parser.py',132),
  ('opt_program -> program','opt_program',1,'p_opt_program','parser.py',136),
  ('opt_program -> empty','opt_program',1,'p_opt_program','parser.py',137),
  ('program -> program statement','program',2,'p_program','parser.py',141),
  ('program -> statement','program',1,'p_program','parser.py',142),
  ('statement -> assignment','statement',1,'p_statement','parser.py',149),
  ('statement -> port_property','statement',1,'p_statement','parser.py',150),
  ('statement -> link','statement',1,'p_statement','parser.py',151),
  ('statement -> define_rule','statement',1,'p_statement','parser.py',152),
  ('statement -> group','statement',1,'p_statement','parser.py',153),
  ('statement -> apply','statement',1,'p_statement','parser.py',154),
  ('assignment -> IDENTIFIER COLON qualified_name LPAREN named_args RPAREN','assignment',6,'p_assignment','parser.py',159),
  ('opt_direction -> LBRACK IDENTIFIER RBRACK','opt_direction',3,'p_opt_direction','parser.py',164),
  ('opt_direction -> empty','opt_direction',1,'p_opt_direction','parser.py',165),
  ('port_property -> qualified_port opt_direction LPAREN named_args RPAREN','port_property',5,'p_port_property','parser.py',179),
  ('internal_port_property -> unqualified_port opt_direction LPAREN named_args RPAREN','internal_port_property',5,'p_internal_port_property','parser.py',185),
  ('link -> void GT void','link',3,'p_link_error','parser.py',191),
  ('link -> real_outport GT void','link',3,'p_link','parser.py',199),
  ('link -> void GT real_inport_list','link',3,'p_link','parser.py',200),
  ('link -> real_outport GT inport_list','link',3,'p_link','parser.py',201),
  ('link -> implicit_outport GT inport_list','link',3,'p_link','parser.py',202),
  ('link -> internal_outport GT inport_list','link',3,'p_link','parser.py',203),
  ('void -> VOIDPORT','void',1,'p_void','parser.py',208),
  ('inport_list -> inport_list COMMA inport','inport_list',3,'p_inport_list','parser.py',212),
  ('inport_list -> inport','inport_list',1,'p_inport_list','parser.py',213),
  ('real_inport_list -> inport_list COMMA real_inport','real_inport_list',3,'p_real_inport_list','parser.py',223),
  ('real_inport_list -> real_inport','real_inport_list',1,'p_real_inport_list','parser.py',224),
  ('inport -> real_or_internal_inport','inport',1,'p_inport','parser.py',233),
  ('inport -> transformed_inport','inport',1,'p_inport','parser.py',234),
  ('transformed_inport -> port_transform real_or_internal_inport','transformed_inport',2,'p_transformed_inport','parser.py',238),
  ('implicit_outport -> argument','implicit_outport',1,'p_implicit_outport','parser.py',243),
  ('implicit_outport -> label argument','implicit_outport',2,'p_implicit_outport','parser.py',244),
  ('real_or_internal_inport -> real_inport','real_or_internal_inport',1,'p_real_or_internal_inport','parser.py',249),
  ('real_or_internal_inport -> internal_inport','real_or_internal_inport',1,'p_real_or_internal_inport','parser.py',250),
  ('opt_tag -> AT tag_value','opt_tag',2,'p_opt_tag','parser.py',254),
  ('opt_tag -> empty','opt_tag',1,'p_opt_tag','parser.py',255),
  ('tag_value -> NUMBER','tag_value',1,'p_tag_value','parser.py',259),
  ('tag_value -> STRING','tag_value',1,'p_tag_value','parser.py',260),
  ('real_inport -> opt_tag qualified_port','real_inport',2,'p_real_inport','parser.py',265),
  ('real_outport -> qualified_port','real_outport',1,'p_real_outport','parser.py',270),
  ('internal_inport -> unqualified_port','internal_inport',1,'p_internal_inport','parser.py',276),
  ('internal_outport -> unqualified_port','internal_outport',1,'p_internal_outport','parser.py',282),
  ('port_transform -> SLASH argument SLASH','port_transform',3,'p_port_transform','parser.py',288),
  ('port_transform -> SLASH label argument SLASH','port_transform',4,'p_port_transform','parser.py',289),
  ('qualified_port -> IDENTIFIER DOT IDENTIFIER','qualified_port',3,'p_qualified_port','parser.py',293),
  ('unqualified_port -> DOT IDENTIFIER','unqualified_port',2,'p_unqualified_port','parser.py',297),
  ('label -> COLON identifier','label',2,'p_label','parser.py',302),
  ('named_args -> named_args named_arg COMMA','named_args',3,'p_named_args','parser.py',306),
  ('named_args -> named_args named_arg','named_args',2,'p_named_args','parser.py',307),
  ('named_args -> empty','named_args',1,'p_named_args','parser.py',308),
  ('named_arg -> identifier EQ argument','named_arg',3,'p_named_arg','parser.py',312),
  ('argument -> value','argument',1,'p_argument','parser.py',317),
  ('argument -> identifier','argument',1,'p_argument','parser.py',318),
  ('opt_argnames -> argnames','opt_argnames',1,'p_opt_argnames','parser.py',323),
  ('opt_argnames -> empty','opt_argnames',1,'p_opt_argnames','parser.py',324),
  ('argnames -> argnames COMMA IDENTIFIER','argnames',3,'p_argnames','parser.py',329),
  ('argnames -> IDENTIFIER','argnames',1,'p_argnames','parser.py',330),
  ('identifiers -> identifiers COMMA identifier','identifiers',3,'p_identifiers','parser.py',340),
  ('identifiers -> identifier','identifiers',1,'p_identifiers','parser.py',341),
  ('identifier -> IDENTIFIER','identifier',1,'p_identifier','parser.py',346),
  ('string -> STRING','string',1,'p_string','parser.py',352),
  ('string -> string STRING','string',2,'p_string','parser.py',353),
  ('value -> dictionary','value',1,'p_value','parser.py',357),
  ('value -> array','value',1,'p_value','parser.py',358),
  ('value -> bool','value',1,'p_value','parser.py',359),
  ('value -> null','value',1,'p_value','parser.py',360),
  ('value -> NUMBER','value',1,'p_value','parser.py',361),
  ('value -> string','value',1,'p_value','parser.py',362),
  ('bool -> TRUE','bool',1,'p_bool','parser.py',367),
  ('bool -> FALSE','bool',1,'p_bool','parser.py',368),
  ('null -> NULL','null',1,'p_null','parser.py',373),
  ('dictionary -> LBRACE members RBRACE','dictionary',3,'p_dictionary','parser.py',378),
  ('members -> members member COMMA','members',3,'p_members','parser.py',383),
  ('members -> members member','members',2,'p_members','parser.py',384),
  ('members -> empty','members',1,'p_members','parser.py',385),
  ('member -> string COLON value','member',3,'p_member','parser.py',389),
  ('values -> values value COMMA','values',3,'p_values','parser.py',394),
  ('values -> values value','values',2,'p_values','parser.py',395),
  ('values -> empty','values',1,'p_values','parser.py',396),
  ('array -> LBRACK values RBRACK','array',3,'p_array','parser.py',400),
  ('qualified_name -> qualified_name DOT IDENTIFIER','qualified_name',3,'p_qualified_name','parser.py',404),
  ('qualified_name -> IDENTIFIER','qualified_name',1,'p_qualified_name','parser.py',405),
  ('define_rule -> RULE identifier COLON rule','define_rule',4,'p_define_rule','parser.py',436),
  ('rule -> rule AND rule','rule',3,'p_combine_rule','parser.py',440),
  ('rule -> rule OR rule','rule',3,'p_combine_rule','parser.py',441),
  ('rule -> UNOT rule','rule',2,'p_negate_rule','parser.py',445),
  ('rule -> LPAREN rule RPAREN','rule',3,'p_subrule','parser.py',449),
  ('rule -> identifier','rule',1,'p_rule','parser.py',453),
  ('rule -> predicate','rule',1,'p_rule','parser.py',454),
  ('predicate -> identifier LPAREN named_args RPAREN','predicate',4,'p_predicate','parser.py',458),
  ('apply -> APPLY identifiers COLON rule','apply',4,'p_apply','parser.py',462),
  ('group -> GROUP identifier COLON identifiers','group',4,'p_group','parser.py',468),
]
