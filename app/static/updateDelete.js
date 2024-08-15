// Ensure the DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', function () {
    let prevClickedRow = null;

    // Handle row click
    document.querySelectorAll('.clickable-row').forEach(function (row) {
        row.addEventListener('click', function (event) {
            event.stopPropagation();

            // Remove icons from the previously clicked row, if any
            if (prevClickedRow && prevClickedRow !== this) {
                removeIcons(prevClickedRow);
            }

            // Toggle icons on the clicked row
            if (this.classList.contains('update-delete-icons')) {
                removeIcons(this);
                prevClickedRow = null;
            } else {
                addIcons(this);
                prevClickedRow = this;
            }
        });
    });

    // Remove icons when clicking outside the table
    document.addEventListener('click', function (event) {
        if (prevClickedRow && !event.target.closest('.table')) {
            removeIcons(prevClickedRow);
            prevClickedRow = null;
        }
    });

    // Function to add icons to a row
    function addIcons(row) {
        row.classList.add('update-delete-icons');

        let updateIcon = document.createElement('i');
        updateIcon.className = "fa-solid fa-pen-to-square ms-3";

        let deleteIcon = document.createElement('i');
        deleteIcon.className = "fa-solid fa-trash ms-3"
        deleteIcon.style.cursor = "pointer";
        deleteIcon.addEventListener('click', function (event) {
            event.stopPropagation(); // Prevent the row click event from activating

            // Show the delete modal and populate it with the selected college data
            let collegeCode = row.dataset.code;
            let collegeName = row.dataset.name;
            document.getElementById('collegeName').textContent = collegeName;
            document.getElementById('collegeCode').textContent = collegeCode;
            document.getElementById('hiddenCollegeCode').value = collegeCode;

            let deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
            deleteModal.show();
        });

        row.querySelector('td').appendChild(updateIcon);
        row.querySelector('td').appendChild(deleteIcon);
    }

    // Function to remove icons from a row
    function removeIcons(row) {
        row.classList.remove('update-delete-icons');
        let icons = row.querySelectorAll("i.fa-solid.fa-pen-to-square.ms-3, i.fa-solid.fa-trash.ms-3");
        icons.forEach(function (icon) {
            icon.remove();
        });
    }
})