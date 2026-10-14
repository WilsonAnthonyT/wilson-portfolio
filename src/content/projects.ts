export type Project = {
 slug:string; title:string; kicker:string; category:string; year:string; summary:string;
 description:string; stack:string[]; github?:string; visual:string;
 role:string; highlights:string[]; challenge:string; approach:string[]; learnings:string;
};
export const projects:Project[] = [
 {
  slug:'goal-digger',title:'Goal Digger',kicker:'An intelligent productivity companion',category:'AI / PRODUCT ENGINEERING',year:'Current',
  summary:'An agentic AI productivity app that turns ambitious goals into actionable schedules, built with a Flutter and Firebase stack.',
  description:'A team-built mobile application connecting goal planning, structured milestones, adaptive scheduling, focus sessions and a virtual companion. The application combines user-facing product design with an AI-assisted planning pipeline and deterministic safeguards.',
  stack:['Flutter','Dart','Firebase','Gemini','Genkit','Kotlin'],github:'https://github.com/WilsonAnthonyT/Goal-Digger-App',visual:'/assets/goal-digger.svg',
  role:'Team project. Contributions listed in the résumé: architecture, UI/UX, feature integration, debugging and final demonstration. Exact module ownership to be confirmed.',
  highlights:['Goal validation and AI-generated milestone planning','Adaptive scheduling and calendar workflows','Android-native focus support and virtual companion','Fallback behavior for AI-planning failures'],
  challenge:'How can a goal-planning app turn open-ended goals into realistic, editable actions while remaining usable when AI services fail?',
  approach:['Structure the planning flow around validation, milestones and deterministic scheduling.','Integrate Flutter screens with Firebase authentication, persistence and backend functions.','Support review and adjustment of generated tasks before commitment.','Provide fallback paths for supported AI failures without silently bypassing goal validation.'],
  learnings:'Reliable AI features need explicit boundaries, good failure handling and understandable user controls—not just impressive model outputs.'
 },
 {
  slug:'invasion-requiem',title:'Invasion Requiem',kicker:'A 2D pixel RPG built with C++',category:'SOFTWARE / GAME SYSTEMS',year:'Course project',
  summary:'Led a three-person team building a 2D RPG with multiple gameplay systems. Highest project score among 30 course teams.',
  description:'A C++ course team project combining an interconnected collection of gameplay mechanics, level progression and state management. The project achieved the top score among 30 teams according to the supplied résumé.',
  stack:['C++','OOP','Game State','Team Leadership'],github:'https://github.com/WilsonAnthonyT/NTHU_I2P_II-Final_Project',visual:'/assets/invasion.svg',
  role:'Lead developer, team of three (as stated in résumé).',
  highlights:['Six levels and a variety of gameplay systems','Object-oriented implementation in C++','State and feature integration','Highest project score among 30 course teams'],
  challenge:'How do you make several different gameplay mechanics behave as one coherent, maintainable application?',
  approach:['Organize level and gameplay logic around clear object responsibilities.','Coordinate game state and transitions across different mechanics.','Integrate features built by a team into a consistent playable experience.'],
  learnings:'Complexity is easier to manage when components have clear responsibilities and game state flows are explicit.'
 },
 {
  slug:'8051-runtime',title:'8051 Threading Lab',kicker:'Multithreading in a constrained environment',category:'EMBEDDED / OPERATING SYSTEMS',year:'OS project',
  summary:'Implemented thread creation, yielding, context switches and semaphore synchronization on the 8051.',
  description:'An operating-systems project exploring lightweight threads in the resource-constrained 8051 environment. The work involved low-level C with SDCC, register preservation, timer-driven scheduling, semaphores and producer-consumer synchronization.',
  stack:['C','SDCC','8051','Operating Systems'],visual:'/assets/threads.svg',
  role:'Implemented threading and synchronization functionality as described in résumé; repository link not yet provided.',
  highlights:['Thread creation, yield and termination','Context-switching and register preservation','Timer-driven scheduling','Semaphore and producer-consumer coordination'],
  challenge:'How can independent threads safely share a tiny embedded processor and constrained memory?',
  approach:['Implement threading primitives and context-switching behavior.','Preserve processor state across thread transitions.','Coordinate concurrent tasks with semaphores and a producer-consumer scenario.'],
  learnings:'Operating-system abstractions become much clearer when the scheduling and synchronization mechanisms are implemented close to the hardware.'
 },
 {
  slug:'savewiser',title:'SaveWiser',kicker:'Budgeting with intentional constraints',category:'MOBILE / PRODUCT ENGINEERING',year:'Client project',
  summary:'A Flutter budgeting app developed from client requirements, including financial constraint logic and a savings-lock feature.',
  description:'A mobile budgeting and savings application designed around client requirements. The project includes interface implementation, financial constraint logic, a savings-lock feature and Android build workflows.',
  stack:['Flutter','Dart','Android','UI/UX'],github:'https://github.com/WilsonAnthonyT/SaveWiserApp',visual:'/assets/savewiser.svg',
  role:'Developer — client project (as stated in résumé).',
  highlights:['Translated client requirements into a Flutter application','Budgeting and savings workflows','Financial constraint logic and savings-lock feature','Android builds and release preparation'],
  challenge:'How can a budgeting experience make financial constraints clear without making the application frustrating to use?',
  approach:['Map client requirements to practical application flows.','Design mobile views around budgeting, tracking and savings.','Implement financial rules and a savings-lock interaction.'],
  learnings:'Products improve when implementation decisions are grounded in real user needs and understandable interfaces.'
 }
];
export const getProject = (slug:string) => projects.find(p=>p.slug===slug);
