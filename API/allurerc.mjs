export default {
  name: "API Tests Allure Report",
  output: "./allure-report",
  historyPath: "./history.jsonl",
  qualityGate: {
    rules: [
      {
        maxFailures: 0,
      },
    ],
  },
  plugins: {
    awesome: {
      options: {
        reportName: "API Tests Allure Report",
        singleFile: false,
        reportLanguage: "en",
        open: false,
        publish: true,
      },
    },
  },
};
