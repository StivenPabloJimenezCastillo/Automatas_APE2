const operationSelect = document.getElementById("operation");
const methodSections = document.querySelectorAll(".method-fields");

function updateMethodFields() {
  const selectedOperation = operationSelect.value;

  methodSections.forEach((section) => {
    const isActive = section.dataset.op === selectedOperation;
    section.classList.toggle("active", isActive);

    section.querySelectorAll("input").forEach((input) => {
      input.required = isActive;
      input.disabled = !isActive;
    });
  });
}

operationSelect.addEventListener("change", updateMethodFields);
updateMethodFields();
