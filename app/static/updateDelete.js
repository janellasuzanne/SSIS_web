// Ensure the DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', function () {
    let prevClickedRow = null;
    const currentPage = document.body.getAttribute('data-page');
    console.log("Current page:", currentPage);

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
        updateIcon.style.cursor = "pointer";
        updateIcon.addEventListener('click', function (event) {
            event.stopPropagation();
            openUpdateModal(row);
        })

        let deleteIcon = document.createElement('i');
        deleteIcon.className = "fa-solid fa-trash ms-3"
        deleteIcon.style.cursor = "pointer";
        deleteIcon.addEventListener('click', function (event) {
            event.stopPropagation(); // Prevent the row click event from activating
            openDeleteModal(row);
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

    function openUpdateModal(row) {
        let modalId;
        switch (currentPage) {
            case 'colleges':
                modalId = 'updateCollegeModal';
                // $('#updateCollegeModal').modal('show');
                break;
            case 'courses':
                $('#updateCourseModal').modal('show');
                break;
            case 'students':
                $('#updateStudentModal').modal('show');
                break;
            default:
                console.error("No matchin modal!");
                return;
        }

        const modal = document.getElementById(modalId);
        if (!modal) {
            console.error("Modal not found!");
            return;
        }

        const dataAttributes = row.dataset;
        for (const key in dataAttributes) {
            if (dataAttributes.hasOwnProperty(key)) {
                const value = dataAttributes[key];
                console.log("Value: ", value);
                console.log("Data Attributes: ", dataAttributes);

                const modalElement = modal.querySelector(`#${key}UpdateInput`);
                console.log("Modal Element: ", modalElement);
                if (modalElement) {
                    modalElement.value = value;
                }

                const hiddenInput = modal.querySelector(`#hidden${capitalizeFirstLetter(key)}`);
                if (hiddenInput) {
                    hiddenInput.value = value;
                }
            }
        }

        // Show the modal
        $(modal).modal('show');
    }

    function openDeleteModal(row) {
        console.log("Opening Delete Modal for page:", currentPage);

        let modalId;
        switch (currentPage) {
            case 'colleges':
                // $('#deleteCollegeModal').modal('show');
                modalId = 'deleteCollegeModal';
                break;
            case 'courses':
                // $('#deleteCourseModal').modal('show');
                modalId = 'deleteCourseModal';
                break;
            case 'students':
                // $('#deleteStudentModal').modal('show');
                modalId = 'deleteStudentModal';
                break;
            default:
                console.error("No matching modal!");
                return;
        }

        const modal = document.getElementById(modalId);

        if (!modal) {
            console.error("Modal not found!");
            return;
        }

        // Get all data attributes from the clicked row
        const dataAttributes = row.dataset;
        console.log("Data Attributes: ", dataAttributes)

        for (const key in dataAttributes) {
            if (dataAttributes.hasOwnProperty(key)) {
                const value = dataAttributes[key];

                // Update modal elements with matching data attributes
                const modalElement = modal.querySelector(`#${key}`);
                console.log("Modal Element: ", modalElement);
                if (modalElement) {
                    modalElement.textContent = value;
                }

                // Update hidden input field, if it exists (e.g., for codes)
                const hiddenInput = modal.querySelector(`#hidden${capitalizeFirstLetter(key)}`);
                console.log("HiddenInput Element: ", hiddenInput);
                if (hiddenInput) {
                    hiddenInput.value = value;
                    console.log("HiddenInput Input: ", hiddenInput.value);
                }
            }
        }
        // // Get the college code and name from the clicked row's data attributes
        // const collegeCode = row.dataset.code;
        // const collegeName = row.dataset.name;

        // // Set the modal's elements with the college data
        // modal.querySelector('#code').textContent = collegeCode;
        // modal.querySelector('#name').textContent = collegeName;

        // // Set the hidden input for the college code in the form
        // const hiddenInput = modal.querySelector('#hiddenCode');
        // hiddenInput.value = collegeCode;

        // Show the modal
        $(modal).modal('show');
    }

    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
})