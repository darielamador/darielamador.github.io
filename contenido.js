// =============================================================
//  CONTENIDO DEL SITIO — este es el único archivo que necesitás editar.
//  1. Subí tus PDFs a  contenido/pdf/   y tus Markdown a  contenido/md/
//  2. Agregá una entrada en la lista correspondiente de abajo.
//
//  Tipos de entrada:
//    { tipo: "pdf",     titulo, descripcion, archivo: "contenido/pdf/x.pdf", fecha }
//    { tipo: "md",      titulo, descripcion, archivo: "contenido/md/x.md",   fecha }
//    { tipo: "enlace",  titulo, descripcion, url: "https://...",            fecha }
//    { tipo: "seccion", id: "sin-espacios", titulo, descripcion, items: [ ...entradas... ] }
//  Una "seccion" abre su propia página y puede contener otras secciones.
//  Los "id" de las secciones deben ser únicos en todo el sitio.
// =============================================================

window.SITIO = {
  perfil: {
    nombre: "Dariel Amador",
    lema: "Economist passionate about Monetary macroeconomics for small open economies", // título grande de Home
    titular: "Economist · MSc Economics, University of Warwick",
    ubicacion: "Coventry, United Kingdom",
    email: "darielamador04@gmail.com",
    linkedin: "https://www.linkedin.com/in/dariel-amador-98657b224/",
    github: "https://github.com/darielamador",
    cv: "contenido/pdf/cv.pdf", // reemplazá este archivo por tu CV
    foto: "assets/perfil.jpg",
    bio: [
      "I am an economist with degrees in Economics and Law from the University of Costa Rica, where I taught introductory economics and economic data courses at the School of Economics.",
      "I am currently pursuing the MSc in Economics at the University of Warwick. My research focuses on applied monetary macroeconomics for small open economies, including wage rigidities, the asymmetric transmission of monetary policy, and the coherence between fiscal and monetary policy in Costa Rica.",
      "Teaching and taking part in research at the University of Costa Rica showed me that this is the work I want to do for the rest of my life. My goal is to pursue a PhD in Economics, specialising in monetary economics and public finance.",
    ],
    intereses: ["Monetary economics", "Public finance", "Small open economies", "DSGE models", "Time-series econometrics", "Law & economics"],
    herramientas: ["Stata", "R", "Python", "Dynare / MATLAB", "LaTeX"],
  },

  // ---------- Pestaña Research ----------
  research: [
    {
      tipo: "pdf",
      titulo: "Wagner's Law in Central America, 1970–2023",
      descripcion: "With Jerlin Villalobos. ARDL and error-correction estimates of the long-run elasticity of public spending to income for Costa Rica, El Salvador, Honduras and Guatemala. Written in Spanish.",
      archivo: "contenido/pdf/wagners-law-central-america.pdf",
    },
    {
      tipo: "wp",
      titulo: "Downward Nominal Wage Rigidity and the Asymmetric Transmission of Monetary Policy: Micro and Macro Evidence for Costa Rica",
      descripcion: "Builds a pseudo-panel of birth-decade, sex and education cohorts from Costa Rica's Continuous Employment Survey (2011–2025) to document how nominal wages adjust, and develops a small open economy New Keynesian DSGE model with an occasionally binding floor on wage cuts, solved with OccBin in Dynare. Because the wage floor binds only after adverse shocks, monetary tightening and easing are transmitted asymmetrically. To my knowledge, the first application of this mechanism to a Central American economy.",
    },
    {
      tipo: "wp",
      titulo: "Asymmetries in Costa Rican Monetary Policy",
      descripcion: "Identifies monetary policy shocks as deviations from three Taylor rule specifications (basic, open economy and with interest rate smoothing) and estimates their effect on economic activity with local projections. Contractionary and expansionary shocks have significantly different effects about 16 to 18 months after impact across all three rules, while asymmetries between expansions and recessions appear earlier and depend more on the rule specification. Updates Mayorga-Martínez et al. (2003) with a sample that includes the global financial crisis and the COVID-19 pandemic.",
    },
  ],

  // ---------- Pestaña Portfolio ----------
  portafolio: [
    {
      tipo: "seccion",
      id: "proofs",
      titulo: "Proofs & derivations",
      descripcion: "Worked proofs and step-by-step model derivations.",
      items: [
        {
          tipo: "seccion",
          id: "maths",
          titulo: "Mathematics",
          descripcion: "Real analysis, optimisation and linear algebra.",
          items: [],
        },
        {
          tipo: "seccion",
          id: "econometrics",
          titulo: "Econometrics",
          descripcion: "Proofs from the MSc econometrics sequence.",
          items: [
            {
              tipo: "md",
              titulo: "OLS is unbiased and consistent",
              descripcion: "Proof and sampling distributions for n = 20, 100 and 1000.",
              archivo: "contenido/md/ols-unbiased-consistent.md",
            },
            {
              tipo: "md",
              titulo: "The Law of Large Numbers and the Central Limit Theorem",
              descripcion: "Proofs and Monte Carlo simulations in Python.",
              archivo: "contenido/md/lln-clt.md",
            },
          ],
        },
        {
          tipo: "seccion",
          id: "macro",
          titulo: "Macroeconomic models",
          descripcion: "Full derivations of standard macro models.",
          items: [
            {
              tipo: "md",
              titulo: "Full derivation of the New Keynesian model",
              descripcion: "Households, the dynamic IS curve, Calvo pricing and the New Keynesian Phillips Curve.",
              archivo: "contenido/md/modelo-neokeynesiano.md",
              fecha: "2026",
            },
          ],
        },
      ],
    },
    {
      tipo: "enlace",
      titulo: "Code on GitHub",
      descripcion: "Scripts and replication files in Stata, R, Python and Dynare.",
      url: "https://github.com/darielamador",
    },
  ],

  // ---------- Pestaña Teaching ----------
  teaching: [
    {
      curso: "EC-1100 · Introducción a la Economía",
      lugar: "School of Economics, University of Costa Rica",
      rol: "Instructor",
      descripcion: "Introductory course covering supply and demand, market structures and basic macroeconomics.",
      materiales: [
        // { tipo: "pdf", titulo: "Syllabus", archivo: "contenido/pdf/ec1100-syllabus.pdf" },
      ],
    },
    {
      curso: "EC-4101 · Datos Económicos",
      lugar: "School of Economics, University of Costa Rica",
      rol: "Instructor",
      descripcion: "Applied course on economic data sources, measurement and empirical assignments.",
      materiales: [],
    },
  ],

  // ---------- Teaching assistant ----------
  asistencias: [
    { curso: "Teoría Macroeconómica I", lugar: "School of Economics, University of Costa Rica", rol: "Teaching assistant" },
    { curso: "Computación para Economistas", lugar: "School of Economics, University of Costa Rica", rol: "Teaching assistant" },
    { curso: "Teoría de Juegos", lugar: "School of Economics, University of Costa Rica", rol: "Teaching assistant" },
  ],
};
