---
title: Getting Started with FAST
description: A guide to setting up your FAST development environment and deploying your first module
author: FAST Team
date: 2026-02-19
tags: [getting-started, setup, environment, tutorial]
---

This guide will walk you through setting up a **FAST** development environment and deploying your first module. You'll learn how to install the Core module foundation and then add specialized modules to build enterprise applications on Microsoft Power Platform / Dynamics 365.

**Note:** This guide covers the manual setup approach. Future articles will detail automated scripting methods and synchronization with source control systems.

## Prerequisites

Before you begin, ensure you have:

- Access to a Microsoft Power Platform or Dynamics 365 environment
- System administrator or System Customizer privileges in your target environment
- Basic familiarity with Dataverse concepts
- Downloaded FAST module solution files from the [FAST Modules Repository](https://github.com/microsoft/industry-apps)

## Phase 1: Install the Core Module

The Core module provides the foundational components that other FAST modules depend on. Install it first in any new environment.

### Step 1: Environment Setup

**Provision or select your target environment:**
- Create a new Dataverse environment through the Power Platform Admin Center, or
- Choose an existing development/sandbox environment
- Ensure the environment has sufficient storage and user licenses for your needs

### Step 2: Install Core Module

1. **Download the Core module** from the [FAST Modules Repository](https://github.com/microsoft/industry-apps)
   - Navigate to the releases section
   - Download the latest Core module managed solution (e.g., `Core_v1.0.0.0_managed.zip`)

2. **Import the Core module solution**
   - Open the [Power Platform Admin Center](https://admin.powerplatform.microsoft.com)
   - Navigate to your target environment
   - Select **Solutions** from the left navigation
   - Click **Import** and select the downloaded Core module file
   - Follow the import wizard prompts
   - Wait for the import to complete successfully

3. **Verify installation**
   - Check that the Core solution appears in your solutions list
   - Review the solution components (tables, apps, flows)
   - Confirm no import errors or warnings

### Step 3: Configure Connections

Create and configure the following standard connections for FAST modules:

- **Microsoft Dataverse** - Core data storage and operations
- **SharePoint** - Document management and collaboration (if using document features)
- **Office 365 Outlook** - Email integration and notifications (if using email features)
- **Microsoft Teams** - Team collaboration and notifications (if using Teams integration)

**Note:** Not all connections are required for all modules. Configure only those connections needed by the specific modules you plan to deploy. Each module's documentation will list its required connections.

### Step 4: Test the Core Module

1. Open the Core module app from your environment
2. Verify that basic navigation and functionality work correctly
3. Confirm that core reference data (if any) is available
4. Test any included sample data or configurations

## Phase 2: Add Specialized Modules

Once your Core module is installed, you can add specialized modules based on your organization's needs.

### Step 1: Select Your Modules

Browse the [Modules]({{ '/modules/' | relative_url }}) area to explore available FAST modules:

- **Asset Management** - Track and manage resources throughout their lifecycle
- **Training and Certification** - Manage training programs and compliance
- **Project Tracking** - Manage tasks, milestones, and deliverables
- **Time & Expense Tracking** - Capture time entries and expenses
- And many more...

Each module page provides:
- Overview and features
- Data model diagrams
- Download links for latest releases
- Deployment documentation

### Step 2: Install Additional Modules

For each selected module:

1. **Download the module solution** from the repository
2. **Review dependencies** - ensure any required modules are already installed
3. **Import the solution** through the Power Platform Admin Center
4. **Configure module-specific settings** as documented
5. **Create required connections** if any new connectors are needed
6. **Test the module** to verify proper installation

### Step 3: Create Your Custom Solution

To build your own application using FAST modules:

1. **Create a new unmanaged solution** for your specific application
   - Use a clear naming convention (e.g., `YourOrg-AssetTracking-v1`)
   - Add a meaningful description and version information
   - Set appropriate solution publisher details

2. **Add FAST components to your solution**
   - Add existing components (tables, forms, views) from installed modules
   - Customize as needed for your requirements
   - Build additional components specific to your use case

3. **Customize and extend**
   - Modify forms, views, and business logic
   - Add custom fields to existing tables
   - Create new automation flows
   - Configure security roles and permissions

4. **Test thoroughly**
   - Validate all functionality in your development environment
   - Test integration points between modules
   - Verify security and permissions

## Best Practices

### Solution Layering

FAST modules use a layered approach:
- **Managed solutions** (Core and specialty modules) provide the base functionality
- **Unmanaged solutions** (your customizations) extend and modify as needed
- Keep customizations in separate solutions for easier maintenance and upgrades

### Environment Strategy

Consider this environment progression:
1. **Development** - Install modules, build customizations, test changes
2. **Test/UAT** - Deploy for user acceptance testing
3. **Production** - Deploy validated solutions for end users

### Module Updates

When new versions of FAST modules are released:
1. Review release notes for breaking changes
2. Test updates in a development environment first
3. Validate your customizations still work
4. Deploy to production following your ALM process

## Next Steps

After completing this setup:

1. **Explore module documentation** for detailed feature guides
2. **Review [Use Cases]({{ '/use-cases/' | relative_url }})** for real-world scenarios
3. **Join the community** to share experiences and get help
4. **Plan your ALM strategy** for moving solutions between environments
5. **Consider contributing** improvements back to the FAST repository

## Getting Help

If you encounter issues during setup:

- Review the module-specific documentation on this site
- Check the [FAST Modules Repository](https://github.com/microsoft/industry-apps) for known issues
- Refer to our [Support page]({{ '/SUPPORT' | relative_url }}) for information on filing issues
- Engage with the community through repository discussions

---

**Welcome to FAST!** We're excited to see what you build.
