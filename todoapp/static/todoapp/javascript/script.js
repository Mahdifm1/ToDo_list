let checkboxes = document.querySelectorAll("input[type='checkbox']");

let currentCheckboxId = null;

for (let i = 0; i < checkboxes.length; i++) {
    let checkbox = checkboxes[i];
    checkbox.addEventListener("change", function () {
        // Get the task_id of the checkbox that was changed.
        currentCheckboxId = this.id;
        window.location.href = "/change/" + currentCheckboxId + "/";

    });
    currentCheckboxId = null;
}
